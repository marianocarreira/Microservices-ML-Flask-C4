import json, os

flask_env = os.environ.get('FLASK_ENV', 'development')

if flask_env == "development":
    configPath = "./config.json"
else:
    configPath = "./config_docker.json"

with open(configPath) as config_file:
    config_data = json.load(config_file)
    print(config_data)