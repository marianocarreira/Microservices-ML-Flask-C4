from flask import request, jsonify, abort
from . import predictor_internal_api_blueprint, theCache, make_predictor_key
from domain import predictor_service as svc
from infrastructure.config import config_data

@predictor_internal_api_blueprint.route(f'{config_data["API_BASE_URL"]}/riesgoCardiaco', methods=['GET'])
@theCache.cached(timeout=60, make_cache_key=make_predictor_key)
def riesgo_cardiaco_get():
    params = svc.ModelParams()
    error = params.fromRequest(request)
    if error:
        return jsonify(error),400
    
    riesgo = svc.calcularRiesgoLight(params)
    riesgo = round(riesgo)
    riesgo_response='No existe riesgo cardíaco'
    if riesgo > 0:
        riesgo_response = 'Si, existe riesgo cardíaco'

    return jsonify({"riesgo_cardiaco":riesgo_response}) 