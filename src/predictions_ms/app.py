from api import createApp

app = createApp()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8010,debug=True,threaded=True) 
