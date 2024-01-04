from infrastructure.users_model import User

class AuthResponse:
    def __init__(self, user, status):
        self.user = user
        self.status = status

def authUser(api_Key):
    user_returned = User.query.filter_by(apiKey=api_Key).first()
    status = 'No Autorizado'
    if user_returned:
        status='Ok'
    return AuthResponse(user_returned,status)
    