from flask import Blueprint
from flask import Flask
from flask_migrate import Migrate
from infrastructure import db
from infrastructure.users_model import User

users_internal_api_blueprint = Blueprint('users_internal_api_blueprint', __name__)

def createApp():
    app = Flask(__name__)

    # configure application
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@127.0.0.1:5432/users-db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql10675102:Xv7sb2wbBx@sql10.freesqldatabase.com/sql10675102'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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