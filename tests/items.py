import requests
from datetime import datetime


def post_request_ext():
    url = f"http://192.168.60.203:8001/items/"
    for item in range(0, 10000):

        data = {
            "name": f"user-{ item }",
            "description": f"{ datetime.now() }"
        }

        response = requests.post(url, json=data)
        print(response.text)


post_request_ext()