"""http request with proxies"""
import requests


def get_proxies():
    proxies = dict(
        http='http://user:passwd@isas.danskenet.net:80',
        https='http://user:passwd@isas.danskenet.net:80',
    )
    return proxies


if __name__ == '__main__':
    url = 'http://google.com'
    response = requests.get(url) #proxies=get_proxies())

    print(response.status_code)
    print()
    print(response.headers)
    print()
    print(response.content)
