import pika, json, time
from datetime import datetime
from flask import request

def queue_logMessage(time,endpoint,statusStr,statusCode, apiKey):
    try:
        params = pika.ConnectionParameters(
                    host='localhost',  
                    port=5672,         
                    virtual_host='/',
                    credentials=pika.PlainCredentials(username='root', password='root'))
        
      
        otherparam = pika.URLParameters("amqps://juvsiwic:BsycWVEIccDJ-7cW1_ysrA_1vXp57YQ4@prawn.rmq.cloudamqp.com/juvsiwic")
        connection=pika.BlockingConnection(otherparam)
        print("Connected to RabbitMQ!")
        
        channel = connection.channel()
        channel.queue_declare(queue='queue-log')
        if statusStr=='error':
            dataTypeVble = 2
        else:
            dataTypeVble = 1
        entry =  json.dumps({
            "datetime": str(datetime.utcnow()),
            "data": json.dumps({ "apiKey": apiKey, "status": statusStr, "statusCode": statusCode,"enlapsedTimeInMs": str(time), "endpoint": endpoint },default=str),
            "dataType": dataTypeVble
        },default=str) 
        channel.basic_publish(exchange='', routing_key='queue-log' ,body=str(entry))
        print(f"Published message: {entry}")
        connection.close()
    except Exception as e:
        print(f"Error sending message to the queue. {e}")
