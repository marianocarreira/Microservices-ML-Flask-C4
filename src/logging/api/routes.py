from flask import request
from .  import logging_internal_api_blueprint
from domain import logger_service as svc
from flask import jsonify
from infrastructure.logger_consumer import start_consuming

@logging_internal_api_blueprint.route('/internal/api/log', methods=['GET'])
def log_get():
    return svc.getLogs()
    
@logging_internal_api_blueprint.route('/internal/api/log/create', methods=['POST'])
def log_create_post():
    return svc.postLog()

@logging_internal_api_blueprint.route('/internal/api/log/start', methods=['GET'])
def log_start():
    return start_consuming("queue-log")