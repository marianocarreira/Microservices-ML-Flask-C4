from . import users_model as model
from . import db

def seedUsers(app):
    with app.app_context():
        users = [
            model.User(apiKey='1234',suscriptionName="FREEMIUM",suscriptionRpm=5),
            model.User(apiKey='4321',suscriptionName="PREMIUM",suscriptionRpm=50)
        ]

        shouldCommit = False
        for user_data in users:
            key = user_data.apiKey

            # Check if the user already exists
            existing_user = model.User.query.filter_by(apiKey=key).first()

            if not existing_user:
                db.session.add(user_data)
                shouldCommit = True
            
        if shouldCommit == True:
            db.session.commit()
