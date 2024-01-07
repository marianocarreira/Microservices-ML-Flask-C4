from infrastructure.users_model import User
from api import createApp 
from domain.users_service import User 
from infrastructure.config import config_data

app = createApp()

if __name__ == '__main__':
     app.run(host=config_data["APP_HOST"],port=config_data["APP_PORT"],debug=True,threaded=True) 
   
    