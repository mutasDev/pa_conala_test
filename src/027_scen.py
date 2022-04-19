#download a file `url` over HTTP and save to `file_name`


import urllib.request

urllib.request.urlretrieve("http://example.com/file.zip", "file_name.zip")