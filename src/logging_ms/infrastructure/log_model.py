from datetime import datetime
from . import db

class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dataType = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Text, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'datetime': self.datetime,
            'datatType': self.dataType,
            'data': self.data
        }