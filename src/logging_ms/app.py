from api import createApp 
from infrastructure.logger_consumer import start_consuming
import threading
from infrastructure.config import config_data
from infrastructure.waiter import wait_for_port

wait_for_port("pg_container","5432")
wait_for_port("rabbitmqServer","5672")

app = createApp()

if __name__ == '__main__':
    QUEUE_LOG_NAME=config_data["LOG_QUEQUE_NAME"]
    thr = threading.Thread(target=start_consuming, kwargs={'queueName':QUEUE_LOG_NAME,'app':app})
    thr.start()
    app.run(host=config_data["APP_HOST"],port=config_data["APP_PORT"],debug=True,threaded=True) 
    thr.join()
