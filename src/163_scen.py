#Send a post request with raw data `DATA` and basic authentication with `username` and `password`


import requests

url = 'https://example.com/api/v1/endpoint'

DATA = {'key1': 'value1', 'key2': 'value2'}

username = 'your-username'
password = 'your-password'

response = requests.post(url, DATA, auth=(username, password))