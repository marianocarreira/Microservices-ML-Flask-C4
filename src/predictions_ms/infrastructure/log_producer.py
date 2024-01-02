import pika
from datetime import datetime
from flask import jsonify
def queue_logMessage(time):
    params = pika.ConnectionParameters(
                host='localhost',  
                port=5672,         
                virtual_host='/',
                credentials=pika.PlainCredentials(username='root', password='root')
                )
    connection=pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='queue-log')
    channel.basic_publish(exchange='', routing_key='queue-log' ,body=str(time))
    connection.close()
