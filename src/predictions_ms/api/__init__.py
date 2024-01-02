from flask import Blueprint, request
import time
from flask_caching import Cache
from infrastructure.log_producer import queue_logMessage

predictor_internal_api_blueprint = Blueprint('predictor_internal_api', __name__)
theCache = Cache(config={'CACHE_TYPE': 'SimpleCache'})   

from . import controller
from flask import Flask

class TimingMiddleware:
    def __init__(self, flaskApp):
        self.app = flaskApp.wsgi_app
      
    def __call__(self, environ, start_response):
        start_time = time.time()
        response = self.app(environ, start_response)
        end_time = time.time()
        elapsed_time = end_time - start_time
        queue_logMessage(elapsed_time)
        return response

def createApp():
    app = Flask(__name__)
    # Register blueprints
    from api import predictor_internal_api_blueprint, theCache

    theCache.init_app(app)
    app.register_blueprint(predictor_internal_api_blueprint)
    app.wsgi_app = TimingMiddleware(app)

    # import declared routes
    from . import controller
    return app