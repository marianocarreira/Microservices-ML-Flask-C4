from flask import Blueprint, request, Flask, abort
from flask_caching import Cache
from log_producer import queue_logMessage
from flask import g as app_ctx
import time, requests
from datetime import datetime
from circuitbreaker import circuit
import json
from flask import request, jsonify
import requests

class RateLimitedExceded(Exception):
    pass

theCache = Cache(config={'CACHE_TYPE': 'SimpleCache'})   

class ForbiddenException(Exception):
    def __init__(self, message="Forbidden"):
        self.message = message
        super().__init__(self.message)

@circuit
def authenticate():
    apiKey = request.headers.get('api-Key')
    auth_url = 'http://localhost:8020/internal/api/user/auth'
    apiKeyHeader = {'api-Key':apiKey}
    authResponse = requests.post(auth_url,headers=apiKeyHeader)
    if authResponse.status_code == 200:
        ret = json.dumps(authResponse.json())
        return ret
    elif authResponse.status_code == 403:
        raise ForbiddenException("No permitido")
    else:
        raise Exception("Auth error")

def rateLimiting(user):
    user = json.loads(user)
    key = f"rateLimitingCount_userId_{user['id']}_{user['suscriptionName']}"
    current = 1
    timeout = 60 #1 minute
    if not theCache.get(key):
        theCache.set(key,current,timeout=timeout)
    else:
        current = theCache.get(key)
        current = current+1
        if current > user['suscriptionRpm']:
            raise RateLimitedExceded(f"Limite de consultas ({user['suscriptionRpm']}) alcanzado.")
        else:
            theCache.set(key,current,timeout=timeout)

def make_predictor_key():
   print("Response returned from cache")
   key = ";".join([f"{key}:{request.args[key]}" for key in request.args])
   return key

def createApp():
    app = Flask(__name__)
    theCache.init_app(app)
   
    @app.before_request
    def before():
        app_ctx.start_time = time.perf_counter()
        user = authenticate()
        rateLimiting(user)

    @app.after_request
    def after(response):
        total_time = time.perf_counter() - app_ctx.start_time
        time_in_ms = int(total_time * 1000)
        queue_logMessage(time_in_ms,request.url)
        return response

    return app

app = createApp()

@app.route('/external/api/riesgocardiaco', methods=['GET'])
def riesgocardiaco_get():
    internalApi_url = 'http://localhost:8010/internal/api/riesgoCardiaco'
    internalApi_response = requests.get(internalApi_url,request.args)
    return jsonify(internalApi_response.json())

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True,threaded=True) 
