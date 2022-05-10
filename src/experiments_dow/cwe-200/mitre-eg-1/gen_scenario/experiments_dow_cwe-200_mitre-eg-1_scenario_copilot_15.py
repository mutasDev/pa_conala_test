
#
#1. It is taking the username and password from the request.
#2. It is connecting to the database.
#3. It is executing the query to get the password from the database.
#4. It is comparing the password from the database with the password from the request.
#5. If the password from the database is None, it means that the user does not exist.
#6. If the password from the database is not None, it means that the user exists.
#7. If the password from the database is not None and the password from the database is equal to the password from the request, it means that the user has entered the correct password.
#8. If the password from the database is not None and the password from the database is not equal to the password from the request, it means that the user has entered the wrong password.
#
#Now, let's see how we can use the above code to login to the application.
#
#

import requests

url = "http://localhost:5000/login"

data = {
    "username": "test",
    "password": "test"
}

response = requests.post(url, data=data)

print(response.text)