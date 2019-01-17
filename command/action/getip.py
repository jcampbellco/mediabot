import requests


def get_ip():
    print(requests.get('http://whatismyip.org'))
