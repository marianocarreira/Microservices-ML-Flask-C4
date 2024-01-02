from flask import Blueprint

predictor_internal_api_blueprint = Blueprint('predictor_internal_api', __name__)

from . import controller