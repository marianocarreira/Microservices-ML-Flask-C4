from infrastructure.users_model import User
from infrastructure import db

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

def getAllAsJson():
    jsonUsers = []
    allUsers = User.query.all()
    for u in allUsers:
        jsonUsers.append(u.to_json())
    return jsonUsers 

def addUser(request):
     api_key = request.form.get('apiKey', '1111')
     subscription_name = request.form.get('subscriptionName', 'OTHER')
     subscription_rpm = int(request.form.get('subscriptionRpm'), 0)
     new_user = User(apiKey=api_key, suscriptionName=subscription_name, suscriptionRpm=subscription_rpm)
     db.session.add(new_user)
     db.session.commit()
     return new_user.to_json()

def deleteUser(id):
    user = User.query.get(id)
    if user:
        # Delete the user from the database
        db.session.delete(user)
        db.session.commit()
