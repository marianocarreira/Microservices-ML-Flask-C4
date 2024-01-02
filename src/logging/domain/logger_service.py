from infrastructure import db
from infrastructure.log_model import LogEntry
from datetime import datetime
from flask import jsonify
import json

def getLogs():
    data = []
    for row in LogEntry.query.all():
        data.append(row.to_json())
    response = jsonify(data)
    return response

def postLog(json):
    logEntry = LogEntry() 
    logEntry.data = json['data']
    logEntry.datetime = json['datetime']
    logEntry.dataType = json['dataType']
    db.session.add(logEntry)
    db.session.commit()
    return jsonify({'message': 'User added', 'result': logEntry.to_json()})