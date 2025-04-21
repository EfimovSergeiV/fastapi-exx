import requests
from datetime import datetime



def get_request():
    for item in range(0, 500):
        url = f"http://127.0.0.1:8000/items/{ item }?q=somequery"
        response = requests.get(url)
        print(response.text)


def post_request():
    url = f"http://127.0.0.1:8000/echo/"
    for item in range(0, 10):
        data = {"message": "Hello", "data": { "key": item }}

        response = requests.post(url, json=data)
        print(response.text)

def post_request_ext():
    url = f"http://192.168.60.203:8001/echo/"
    for item in range(0, 10000):
        data = {"message": "Hello", "data": { "key": item }}

        response = requests.post(url, json=data)
        print(response.text)


post_request_ext()