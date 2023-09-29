from MISW_EXP_2_GESTION_EMPRESARIAL import create_app
from flask_restful import Resource, Api
from .util import generate_random_request, simulated_data
import json
import requests

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

with app.app_context():
    request_data = []

    for i in range(97):
        request_data.append(generate_random_request())
    request_data = request_data + simulated_data()

    for item in request_data:
        url = "http://127.0.0.1:5000/api/detector-intrusos"
        data_to_send = json.dumps(item)
        response = requests.post(url, data=data_to_send, headers={"Content-Type": "application/json"})
        print(f'response.status_code: {response.status_code}')
