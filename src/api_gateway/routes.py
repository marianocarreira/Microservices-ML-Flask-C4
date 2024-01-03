from flask import request, response
import requests
from .  import app

@app.route('/external/api/riesgocardiaco', methods=['GET'])
def forward_to_api1():
    internalApi_url = 'http://localhost:8080/internal/api/riesgocardiaco'
    internalApi_response = requests.request(request.method)
    #return api1_response.text
    return "aa"

@app.route('/external/api/test', methods=['GET'])
def forward_to_api1():
    return "aa"