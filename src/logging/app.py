from flask import Flask, request, abort

app = Flask(__name__)

# Register blueprints
from api import logging_internal_api_blueprint

app.register_blueprint(logging_internal_api_blueprint)

# import declared routes
from api import routes

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug=True,threaded=True)