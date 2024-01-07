from flask import Blueprint
from flask import Flask
from flask_migrate import Migrate
from infrastructure import db
from infrastructure.users_model import User
from infrastructure.config import config_data

users_internal_api_blueprint = Blueprint('users_internal_api_blueprint', __name__)

def createApp():
    app = Flask(__name__)
   
    # configure application
    app.config.update(config_data)
    
    # Database
    db.init_app(app)
    migrate = Migrate() 
    migrate.init_app(app, db)

    # Register blueprints
    from api import users_internal_api_blueprint
    # import declared routes
    from . import controllers
    app.register_blueprint(users_internal_api_blueprint)
    
    return app