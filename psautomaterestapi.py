import requests
from pprint import pprint as pp


# import json


def demo_get():
    uri = 'https://reqres.in/api/users?page=2'
    response = requests.get(uri)
    print(response.json())  # json 2 py type
    # print(json.loads(response.content.decode()))  # json 2 py type


if __name__ == '__main__':
    demo_get()
