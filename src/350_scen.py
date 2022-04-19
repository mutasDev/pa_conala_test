#send multipart encoded file `files` to url `url` with headers `headers` and metadata `data`


import requests

url = 'http://example.com/upload'
files = {'file': open('test.txt', 'rb')}
headers = {'Content-Type': 'multipart/form-data'}
data = {'user': 'test'}

r = requests.post(url, files=files, headers=headers, data=data)