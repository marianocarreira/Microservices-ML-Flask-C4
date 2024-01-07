from flask import Blueprint
from flask import Flask
from flask_migrate import Migrate
from infrastructure import db
from infrastructure.log_model import LogEntry

logging_internal_api_blueprint = Blueprint('logging_internal_api', __name__)
from . import controller

def createApp():
    app = Flask(__name__)

    # configure application
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@127.0.0.1:5432/logging-db'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql10675102:Xv7sb2wbBx@sql10.freesqldatabase.com/sql10675102'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:tpTopicos2@logging-db.c7o6yioc2vzv.us-east-1.rds.amazonaws.com/logging-db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://agefnoif:LIR1-NUVI-DKTOvKq-eH0li0wpAREWw2@babar.db.elephantsql.com/agefnoif'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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