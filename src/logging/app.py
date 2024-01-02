from application import createApp 
from infrastructure.logger_consumer import start_consuming
import threading    

app = createApp()

if __name__ == '__main__':
    thr = threading.Thread(target=start_consuming, kwargs={'queueName':"queue-log",'app':app})
    thr.start()
    app.run(host="0.0.0.0",port=8000,debug=True,threaded=True) 
    thr.join()
