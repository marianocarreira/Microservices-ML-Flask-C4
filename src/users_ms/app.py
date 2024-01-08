from infrastructure.users_model import User
from api import createApp 
from domain.users_service import User 
from infrastructure.config import config_data
from infrastructure.waiter import wait_for_port
from infrastructure.seeder import seedUsers

wait_for_port("pg_container","5432")

app = createApp()

if __name__ == '__main__':
     seedUsers(app)
     app.run(host=config_data["APP_HOST"],port=config_data["APP_PORT"],debug=True,threaded=True) 
