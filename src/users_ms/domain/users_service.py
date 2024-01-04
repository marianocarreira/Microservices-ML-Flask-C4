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
    if not user_returned:
        return None
    
    user = User()
    user.apiKey = user_returned.apiKey
    user.id = user_returned.id
    user.suscriptionName = user_returned.suscriptionName
    user.suscriptionRpm = user_returned.suscriptionRpm
    return user
    