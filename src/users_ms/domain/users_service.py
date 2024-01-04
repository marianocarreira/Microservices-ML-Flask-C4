from infrastructure.users_model import User

class AuthResponse:
    def __init__(self, user, status):
        self.user = user
        self.status = status
    
    def to_json(self):
        return {
            'user': self.user,
            'status': self.status
        }

def authUser(api_Key):
    user_returned = User.query.filter_by(apiKey=api_Key).first()
    user = User()
    user.apiKey = user_returned.apiKey
    user.id = user_returned.id
    user.suscription_name = user.suscription_name
    user.suscription_rpm = user.suscription_rpm
    status = 'No Autorizado'
    if user_returned:
        status='Ok'
    return AuthResponse(user.to_json(),status)
    