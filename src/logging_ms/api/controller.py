from flask import request
from .  import logging_internal_api_blueprint
from domain import logger_service as svc
from infrastructure.config import config_data

@logging_internal_api_blueprint.route(f'{config_data["API_BASE_URL"]}/log', methods=['GET'])
def log_get():
    return svc.getLogs()
