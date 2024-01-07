import pika, time
from domain import logger_service
import sys, os, json

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
            rabbitmq_params = pika.ConnectionParameters(
            host='localhost', 
            port=5672,       
            virtual_host='/',
            credentials=pika.PlainCredentials(username='root', password='root')
            )
            connection = None
            #while connection is None or not connection.is_open:
            #    try:
            otherparam = pika.URLParameters("amqps://juvsiwic:BsycWVEIccDJ-7cW1_ysrA_1vXp57YQ4@prawn.rmq.cloudamqp.com/juvsiwic")
            connection = pika.BlockingConnection(otherparam)
            #        print("Connected to RabbitMQ!")
            #    except pika.exceptions.AMQPConnectionError:
            #        print("Failed to connect. Retrying in 15 second...")
            #        time.sleep(15)

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
        
