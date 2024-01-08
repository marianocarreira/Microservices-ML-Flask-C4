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
import configuration as config 
import waiter as waiter

waiter.wait_for_port("rabbitmqServer","5672")

class RateLimitedExceded(Exception):
    pass

class ApiResponse():
    def __init__(self):
        self.status = 'ok'
        self.jsonData = None
    
    def to_json(self):
         return {
            'status': self.status,
            'data': self.data
        }
    
theCache = Cache(config={'CACHE_TYPE': config.config_data["CACHE_TYPE"]})   

class ForbiddenException(Exception):
    def __init__(self, message="Forbidden"):
        self.message = message
        super().__init__(self.message)

@circuit
def authenticate():
    API_KEY_HEADER = config.config_data["HEADER_API_KEY"]
    apiKey = request.headers.get(API_KEY_HEADER)
    if not apiKey:
         raise ForbiddenException("No api-Key header detectado")
    AUTH_URL = config.config_data["INTERNAL_AUTH_ENDPOINT"]
    apiKeyHeader = {API_KEY_HEADER:apiKey}
    authResponse = requests.post(AUTH_URL,headers=apiKeyHeader)
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
    TIMEOUT = config.config_data["RATE_LIMITING_TIME_OUT_SECONDS"]
    if not theCache.get(key):
        theCache.set(key,current,timeout=TIMEOUT)
    else:
        current = theCache.get(key)
        current = current+1
        if current > user['suscriptionRpm']:
            raise RateLimitedExceded(f"Limite de consultas ({user['suscriptionRpm']}) alcanzado.")
        else:
            theCache.set(key,current,timeout=TIMEOUT)

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
        API_KEY_HEADER = config.config_data["HEADER_API_KEY"]
        total_time = time.perf_counter() - app_ctx.start_time
        time_in_ms = int(total_time * 1000)
        apiResponse = ApiResponse()
        apiResponse.data = response.json
        status_code = response.status_code
        if(status_code == 200):
            queue_logMessage(time_in_ms,request.url,'ok',status_code,request.headers.get(API_KEY_HEADER))
            apiResponse.status = 'ok'
        else:
            queue_logMessage(time_in_ms,request.url,'error',status_code,request.headers.get(API_KEY_HEADER)) 
            apiResponse.status = 'error'  

        response = jsonify(apiResponse.to_json())
        response.status_code = status_code
        return response

    @app.errorhandler(ForbiddenException)
    def handle_exception(error):
        apiResponse = {'message': str(error)}
        response = jsonify(apiResponse)
        response.status_code = 403
        return response
    
    @app.errorhandler(RateLimitedExceded)
    def handle_exception(error):
        apiResponse = {'message': str(error)}
        response = jsonify(apiResponse)
        response.status_code = 429
        return response
    
    @app.errorhandler(Exception)
    def handle_exception(error):
        apiResponse = {'message': str(error)}
        response = jsonify(apiResponse)
        response.status_code = 500
        return response
    
    RIESGO_CARDIACO_EXPOSED_URL = (config.config_data["EXTERNAL_API_BASE_URL"]+"/riesgocardiaco")
    @app.route(RIESGO_CARDIACO_EXPOSED_URL, methods=['GET'])
    def riesgocardiaco_get():
        INTERNAL_RIESGO_CARDIACO_ENDPOINT = config.config_data["INTERNAL_RIESGO_CARDIACO_ENDPOINT"]
        internalApi_response = requests.get(INTERNAL_RIESGO_CARDIACO_ENDPOINT,request.args)
        return internalApi_response.json(),internalApi_response.status_code

    return app

app = createApp()

if __name__ == '__main__':
     app.run(host=config.config_data["APP_HOST"],port=config.config_data["APP_PORT"],debug=True,threaded=True) 
 
