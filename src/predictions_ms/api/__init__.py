from flask import Blueprint, request, Flask
from flask_caching import Cache

predictor_internal_api_blueprint = Blueprint('predictor_internal_api', __name__)
theCache = Cache(config={'CACHE_TYPE': 'SimpleCache'})   

def make_predictor_key():
   print("Response returned from cache")
   key = ";".join([f"{key}:{request.args[key]}" for key in request.args])
   return key

def createApp():
    app = Flask(__name__)
    theCache.init_app(app)
    from . import controller
    app.register_blueprint(predictor_internal_api_blueprint)
    return app

app = createApp()