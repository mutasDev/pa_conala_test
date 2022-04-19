#download a file `url` over HTTP


import urllib.request

urllib.request.urlretrieve("http://example.com/songs/mp3.mp3", "mp3.mp3")