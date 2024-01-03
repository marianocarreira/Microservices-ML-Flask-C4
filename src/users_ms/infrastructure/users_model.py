from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Text, nullable=False)
    suscriptionType = db.Column(db.Text, nullable=False, )
    
    def to_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'subscriptionType': self.codigo
        }
    
    __table_args__ = (
        CheckConstraint(
            suscriptionType.in_(['FREEMIUM', 'PREMIUM', 'NONE']),
            name='check_valid_subscription'
        )
    )