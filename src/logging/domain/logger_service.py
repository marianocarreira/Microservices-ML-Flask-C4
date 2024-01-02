from infrastructure import db
from infrastructure.log_model import LogEntry
from datetime import datetime
from flask import jsonify

def getLogs():
    data = []
    for row in LogEntry.query.all():
        data.append(row.to_json())
    response = jsonify(data)
    return response

def postLog():
    logEntry = LogEntry()
    logEntry.data = "{ \"data\": \"test\" }"
    logEntry.datetime = datetime.now()
    logEntry.dataType = 1
    db.session.add(logEntry)
    db.session.commit()
    return jsonify({'message': 'User added', 'result': logEntry.to_json()})