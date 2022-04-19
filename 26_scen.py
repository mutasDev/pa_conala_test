#download a file "http://www.example.com/songs/mp3.mp3" over HTTP and save to "mp3.mp3"


import urllib.request

urllib.request.urlretrieve("http://www.example.com/songs/mp3.mp3", "mp3.mp3")