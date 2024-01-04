from sqlalchemy import CheckConstraint
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    apiKey = db.Column(db.Text, nullable=False)
    suscription_name = db.Column(db.Text, nullable=False, default='FREEMIUM')
    suscription_rpm = db.Column(db.Integer, nullable=False)
    
    def to_json(self):
        return {
            'id': self.id,
            'apiKey': self.apiKey,
            'suscription_name': self.suscription_name,
            'suscription_rpm': self.suscription_rpm
        }
    
    __table_args__ = (
        CheckConstraint(
            suscription_name.in_(['FREEMIUM', 'PREMIUM']),
            name='check_valid_subscription'
        ) ,
    )
    