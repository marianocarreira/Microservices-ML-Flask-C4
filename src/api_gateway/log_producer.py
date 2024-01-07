import pika, json, time
from datetime import datetime
from flask import request
import configuration as config 

QUEUE_NAME = config.config_data["QUEUE_LOG_NAME"]

def queue_logMessage(time,endpoint,statusStr,statusCode, apiKey):
    try:
        otherparam = pika.URLParameters(config.config_data["QUEUE_CONNECTION_STRING"])
        connection=pika.BlockingConnection(otherparam)
        print("Connected to RabbitMQ!")
        
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE_NAME)
        if statusStr=='error':
            dataTypeVble = 2
        else:
            dataTypeVble = 1
        entry =  json.dumps({
            "datetime": str(datetime.utcnow()),
            "data": json.dumps({ "apiKey": apiKey, "status": statusStr, "statusCode": statusCode,"enlapsedTimeInMs": str(time), "endpoint": endpoint },default=str),
            "dataType": dataTypeVble
        },default=str) 
        channel.basic_publish(exchange='', routing_key=QUEUE_NAME ,body=str(entry))
        print(f"Published message: {entry}")
        connection.close()
    except Exception as e:
        print(f"Error sending message to the queue. {e}")
