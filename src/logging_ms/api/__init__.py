from flask import Blueprint
from flask import Flask
from flask_migrate import Migrate
from infrastructure import db
from infrastructure.log_model import LogEntry
from infrastructure.config import config_data

logging_internal_api_blueprint = Blueprint('logging_internal_api', __name__)
from . import controller

def createApp():
    app = Flask(__name__)

    # configure application
    app.config.update(config_data)
  
    # Database
    db.init_app(app)
    migrate = Migrate() 
    migrate.init_app(app, db)

    # Register blueprints
    from api import logging_internal_api_blueprint

    app.register_blueprint(logging_internal_api_blueprint)

    # import declared routes
    from . import controller

    return app