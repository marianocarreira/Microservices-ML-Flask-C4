from flask import request, jsonify, abort, make_response
from .  import users_internal_api_blueprint
from domain import users_service as svc
from infrastructure.config import config_data

USERS_AUTH_ENDPOINT_URL = (config_data["API_BASE_URL"]+"/user/auth")
print(USERS_AUTH_ENDPOINT_URL)
@users_internal_api_blueprint.route(USERS_AUTH_ENDPOINT_URL, methods=['POST'])
def auth_post():
    user = svc.authUser(request.headers.get(config_data["API_KEY_HEADER"]))
    if not user:
        abort(403)
    else:
        return jsonify(user.to_json())

USERS_LIST_ENDPOINT_URL = (config_data["API_BASE_URL"]+"/user")
print(USERS_LIST_ENDPOINT_URL)
@users_internal_api_blueprint.route(USERS_LIST_ENDPOINT_URL, methods=['GET'])
def allusers_get():
    return jsonify(svc.getAllAsJson())

USERS_NEW_ENDPOINT_URL = (config_data["API_BASE_URL"]+"/user")
print(USERS_NEW_ENDPOINT_URL)
@users_internal_api_blueprint.route(USERS_NEW_ENDPOINT_URL, methods=['POST'])
def user_post():
    return jsonify(svc.addUser(request))

USERS_DEL_ENDPOINT_URL = (config_data["API_BASE_URL"]+"/user")
print(USERS_NEW_ENDPOINT_URL)
@users_internal_api_blueprint.route(USERS_NEW_ENDPOINT_URL, methods=['DELETE'])
def user_delete():
    id = request.args.get('id')
    if not id:
        abort(400, 'Id no especificado')
    svc.deleteUser(id)
    return make_response('', 200)