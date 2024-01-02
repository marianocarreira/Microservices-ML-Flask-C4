from flask import request, jsonify, abort
from . import predictor_internal_api_blueprint, theCache
from domain import predictor_service as svc

def make_predictor_key():
   key = ";".join([f"{key}:{request.args[key]}" for key in request.args])
   return key

@predictor_internal_api_blueprint.route('/internal/api/riesgoCardiaco', methods=['GET'])
@theCache.cached(timeout=60, make_cache_key=make_predictor_key)
def riesgo_cardiaco_get():
    params = svc.ModelParams()
    params.colesterol = request.args.get('colesterol')
    params.presion = request.args.get('presion')
    params.glucosa = request.args.get('glucosa')
    params.edad = request.args.get('edad')
    params.sobrepeso = request.args.get('sobrepeso')
    params.tabaquismo = request.args.get('tabaquismo')
    error = params.validar()
    
    if error:
        return abort(400, description=error)
    
    return jsonify({"riesgo_cardiaco":svc.calcularRiesgo(params)}) 