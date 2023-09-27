from MISW_EXP_2_GESTION_EMPRESARIAL import create_app
from flask_restful import Api
from modelos import request_data
import json
import random


app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

with app.app_context():
    def generate_random_request_data():
        http_methods_options = ["post", "get", "put", "delete"]
        http_methods_probability = [0.2, 0.5, 0.2, 0.1]
        clients_options = ["safari", "chrome", "firefox"]
        clients_probability = [0.2, 0.5, 0.3]
        operating_systems_options = ["macos", "windows", "linux"]
        operating_systems_probability = [0.2, 0.5, 0.3]
        ip_addresses_options = ["192.168.1.55", "192.168.1.40", f"192.168.1.{random.randint(1, 255)}"]
        ip_addresses_probability = [0.2, 0.5, 0.3]
        access_datetime_options = [f"2023-04-15T{random.randint(8, 17):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}",
                                   f"2023-04-15T{random.randint(17, 20):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}",
                                   f"2023-04-15T{random.randint(20, 23):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}"]
        access_datetime_probability = [0.2, 0.5, 0.3]

        random_data = {
            "http_method": random.choices(http_methods_options, http_methods_probability)[0],
            "url_endpoint": "/ofertas",
            "client": random.choices(clients_options, clients_probability)[0],
            "operating_system": random.choices(operating_systems_options, operating_systems_probability)[0],
            "ip_address": random.choices(ip_addresses_options, ip_addresses_probability)[0],
            "access_datetime": random.choices(access_datetime_options, access_datetime_probability)[0]
        }

        return request_data(**random_data)


    for i in range(20):
        url = "http://127.0.0.1:5000/api/detector-intrusos"
        request_data = generate_random_request_data()
        data_to_send = json.dumps(request_data.__dict__)
        print(data_to_send)
        #response = requests.post(url, data=data_to_send, headers={"Content-Type": "application/json"})
        #print(f'response.status_code: {response.status_code}')
