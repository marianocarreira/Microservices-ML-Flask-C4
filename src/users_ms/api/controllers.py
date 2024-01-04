from flask import request, jsonify, abort
from .  import users_internal_api_blueprint
from domain import users_service as svc

@users_internal_api_blueprint.route('/internal/api/user/auth', methods=['POST'])
def auth_post():
    user = svc.authUser(request.headers.get('api-Key'))
    if not user:
        abort(403)
    else:
        return jsonify(user.to_json())