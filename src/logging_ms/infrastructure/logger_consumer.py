import pika, time
from domain import logger_service
import sys, os, json
from infrastructure.config import config_data

def callback(ch, method, properties, body):
    try:
        request = body.decode()
        print(f"Request received: {request}")
        newJson = json.loads(request)
        logger_service.postLog(newJson)
    except:
        print("Error consuming message from queue")

def start_consuming(queueName, app):
    with app.app_context():
        try:
            connection = None
            timeout = 0
            while connection is None or not connection.is_open:
                try:
                    otherparam = pika.URLParameters(config_data["QUEUE_CONNECTION_STRING"])
                    connection = pika.BlockingConnection(otherparam)
                    print("Connected to RabbitMQ!")
                except pika.exceptions.AMQPConnectionError:
                    if timeout == config_data["QUEUE_CONNECTION_TIMEOUT"]:
                        raise Exception("Time out connecting to the queue")
                    print("Failed to connect. Retrying in 15 second...")
                    time.sleep(15)
                    timeout = timeout + 1

            channel = connection.channel()
            channel.queue_declare(queue=queueName)  
            channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True)
            channel.start_consuming()
        except KeyboardInterrupt:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
        finally:
            print("Ended consumer app")
        
