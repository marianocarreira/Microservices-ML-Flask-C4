from flask import request, jsonify, abort
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