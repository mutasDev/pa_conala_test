
#
#1. The user enters a username and password.
#2. The username and password are sent to the server.
#3. The server checks the database to see if the username and password are correct.
#4. If the username and password are correct, the server returns the username.
#5. If the username and password are incorrect, the server returns "Incorrect Credentials".
#
#The server is vulnerable to SQL injection.
#
#The server is vulnerable to SQL injection because the username and password are not sanitized before being used in the SQL query.
#
#The server is vulnerable to SQL injection because the username and password are not sanitized before being used in the SQL query.
#
#The server is vulnerable to SQL injection because the username and password are not sanitized before being used in the SQL query.
#
#The server is vulnerable to SQL injection because the username and password are not sanitized before being used in the SQL query.
#
#The server

import requests

url = "http://localhost:5000/login"

username = "admin"
password = "admin"

r = requests.post(url, data={"username":username, "password":password})

print(r.text)