from flask import Blueprint, request, Flask
from flask_caching import Cache
from log_producer import queue_logMessage
from flask import g as app_ctx
import time, requests
from datetime import datetime

class RateLimitedExceded(Exception):
    pass

theCache = Cache(config={'CACHE_TYPE': 'SimpleCache'})   

def authenticate():
    apiKey = request.headers.get('apiKey')
    auth_url = 'http://localhost:8020/internal/api/user/auth'
    user = requests.post(auth_url)
    return user

def rateLimiting(user):
    key = f"rateLimitingCount_userId_{user.id}_{user.suscription_name}"
    current = 1
    timeout = 120 #2 minutes
    if not theCache.get(key):
        theCache.set(key,current,timeout=timeout)
    else:
        current = theCache.get(key)
        current = current+1
        if current > user.suscription_rpm:
            raise RateLimitedExceded(f"Limite de consultas ({user.suscription_rpm}) alcanzado.")
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

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080,debug=True,threaded=True) 


