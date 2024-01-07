from api import app
from infrastructure.config import config_data

if __name__ == '__main__':
    app.run(host=config_data["APP_HOST"],port=config_data["APP_PORT"],debug=True,threaded=True) 
