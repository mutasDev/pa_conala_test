#download a file 'http://www.example.com/' over HTTP


import urllib.request

urllib.request.urlretrieve("http://www.example.com/", "file.html")