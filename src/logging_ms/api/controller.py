from flask import request
from .  import logging_internal_api_blueprint
from domain import logger_service as svc

@logging_internal_api_blueprint.route('/internal/api/log', methods=['GET'])
def log_get():
    return svc.getLogs()
