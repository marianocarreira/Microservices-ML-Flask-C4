from flask import request, jsonify, abort
from . import predictor_internal_api_blueprint, theCache, make_predictor_key
from domain import predictor_service as svc

@predictor_internal_api_blueprint.route('/internal/api/riesgoCardiaco', methods=['GET'])
@theCache.cached(timeout=60, make_cache_key=make_predictor_key)
def riesgo_cardiaco_get():
    params = svc.ModelParams()
    error = params.fromRequest(request)
    if error:
        return jsonify(error),400
    
    return jsonify({"riesgoCardiaco":svc.calcularRiesgo(params)}) 