#get the content of child tag with`href` attribute whose parent has css `someclass`


import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.example.com")
soup = BeautifulSoup(r.content, 'html.parser')

links = soup.find_all("a", {"class": "someclass"})
for link in links:
    print(link.get("href"))