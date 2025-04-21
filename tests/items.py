import requests
from datetime import datetime


def post_request_ext():
    url = f"http://192.168.60.203:8001/items/"
    for item in range(0, 2):

        data = {"name": f"user-{ item }", "data": { "key": item }}

        now = datetime.now()
        formatted = now.strftime("%d.%m %H:%M:%Y")

        data = {
            "name": f"user-{ item }",
            "description": f"{ formatted }"
        }

        response = requests.post(url, json=data)
        print(response.text)


post_request_ext()