#download the file from url `url` and save it under file `file_name`


import urllib.request

url = 'http://www.example.com/'
file_name = 'file.html'

urllib.request.urlretrieve(url, file_name)