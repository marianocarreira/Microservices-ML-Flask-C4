import pika, json
from datetime import datetime

def queue_logMessage(time,app):
    with app.app_context():
        try:
            params = pika.ConnectionParameters(
                        host='localhost',  
                        port=5672,         
                        virtual_host='/',
                        credentials=pika.PlainCredentials(username='root', password='root')
                        )
            connection=pika.BlockingConnection(params)
            channel = connection.channel()
            channel.queue_declare(queue='queue-log')
            entry =  json.dumps({
                "datetime": str(datetime.utcnow()),
                "data": json.dumps({ "enlapsedTime": str(time), "endpoint": "riesgoCardiaco" },default=str),
                "dataType": 1
            },default=str) 
            channel.basic_publish(exchange='', routing_key='queue-log' ,body=str(entry))
            print(f"Published message: {entry}")
            connection.close()
        except:
            print("Error consuming message from queue.")
