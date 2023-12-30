from flask import Blueprint

logging_internal_api_blueprint = Blueprint('logging_internal_api', __name__)

from . import routes