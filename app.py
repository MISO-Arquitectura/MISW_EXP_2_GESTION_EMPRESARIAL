from MISW_EXP_2_GESTION_EMPRESARIAL import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from random import random
import random
import json

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

with app.app_context():

    for i in range(100):
        url = "http://127.0.0.1:5000/api/detector-intrusos"
        request_data = request.generate_random_request()
        data_to_send = json.dumps(request_data)
        print(data_to_send)
        #response = requests.post(url, data=data_to_send, headers={"Content-Type": "application/json"})
        #print(f'response.status_code: {response.status_code}')
