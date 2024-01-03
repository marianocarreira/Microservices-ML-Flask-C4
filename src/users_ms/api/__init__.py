from flask import Blueprint
from flask import Flask
from flask_migrate import Migrate
from infrastructure import db
from users_ms.infrastructure.users_model import User

users_internal_api_blueprint = Blueprint('subscription_internal_api', __name__)
from . import controller

def createApp():
    app = Flask(__name__)

    # configure application
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@127.0.0.1:5432/suscriptions-db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Database
    db.init_app(app)
    migrate = Migrate() 
    migrate.init_app(app, db)

    # Register blueprints
    from api import users_internal_api_blueprint

    app.register_blueprint(users_internal_api_blueprint)

    # import declared routes
    from . import controller

    return app