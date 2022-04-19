#match urls whose domain doesn't start with `t` from string `document` using regex


import re

document = "https://www.google.com https://www.twitter.com https://www.facebook.com"

urls = re.findall(r'https?://(?!t)[^\s]+', document)

print(urls)