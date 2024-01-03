from flask import request
from .  import users_internal_api_blueprint
from domain import users_service as svc

@users_internal_api_blueprint.route('/internal/api/user/auth', methods=['POST'])
def log_get():
    return svc.authUser(request.headers["apiKey"])