from flask import request, jsonify
from .  import users_internal_api_blueprint
from domain import users_service as svc

@users_internal_api_blueprint.route('/internal/api/user/auth', methods=['POST'])
def auth_post():
    return jsonify(svc.authUser(request.form.get('apiKey')))