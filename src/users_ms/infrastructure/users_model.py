from sqlalchemy import CheckConstraint
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    apiKey = db.Column(db.Text, nullable=False)
    suscriptionName = db.Column(db.Text, nullable=False, default='FREEMIUM')
    suscriptionRpm = db.Column(db.Integer, nullable=False)
    
    def to_json(self):
        return {
            'id': self.id,
            'apiKey': self.apiKey,
            'suscriptionName': self.suscriptionName,
            'suscriptionRpm': self.suscriptionRpm
        }
    
    __table_args__ = (
        CheckConstraint(
            suscriptionName.in_(['FREEMIUM', 'PREMIUM']),
            name='check_valid_subscription'
        ) ,
    )
    