#get json data from restful service 'url'


import requests

url = 'http://somerestfulservice.com/api/data'

response = requests.get(url)

data = response.json()