from datetime import datetime
from . import db

class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dataType = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'