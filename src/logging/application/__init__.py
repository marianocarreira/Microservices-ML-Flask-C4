from flask import Flask, request, abort
from flask_migrate import Migrate
from infrastructure import db
from infrastructure.log_model import LogEntry

def createApp():
    app = Flask(__name__)

    # configure application
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@127.0.0.1:5432/logging-db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Database
    db.init_app(app)
    migrate = Migrate() 
    migrate.init_app(app, db)

    # Register blueprints
    from api import logging_internal_api_blueprint

    app.register_blueprint(logging_internal_api_blueprint)

    # import declared routes
    from api import routes

    return app
