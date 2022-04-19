#download a file `url` over HTTP and save to "10MB"


import urllib.request

url = 'http://www.example.com/file.txt'

urllib.request.urlretrieve(url, '10MB')