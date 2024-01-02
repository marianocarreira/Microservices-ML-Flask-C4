from flask import request
from . import predictor_internal_api_blueprint
from domain import predicto_service as svc

@predictor_internal_api_blueprint.route('/internal/api/riesgoCardiaco', methods=['get'])
def log_create_post():
    param1 = request.args.get('param1')
    return svc.calcularRiesgo(param1)