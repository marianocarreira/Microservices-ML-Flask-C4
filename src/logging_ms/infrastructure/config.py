import json

with open('./config.json') as config_file:
    config_data = json.load(config_file)
    print(config_data)