from api import createApp 
from infrastructure.logger_consumer import start_consuming
import threading
from infrastructure.config import config_data

app = createApp()

if __name__ == '__main__':
    QUEUE_LOG_NAME=config_data["LOG_QUEQUE_NAME"]
    thr = threading.Thread(target=start_consuming, kwargs={'queueName':QUEUE_LOG_NAME,'app':app})
    thr.start()
    app.run(host=config_data["APP_HOST"],port=config_data["APP_PORT"],debug=True,threaded=True) 
    thr.join()
