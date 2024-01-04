from infrastructure.users_model import User
from api import createApp 
from domain.users_service import User 

app = createApp()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8020,debug=True,threaded=True) 
    