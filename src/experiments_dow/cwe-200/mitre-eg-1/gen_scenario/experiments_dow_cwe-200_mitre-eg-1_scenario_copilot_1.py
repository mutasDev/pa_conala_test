
#
#1.  The user enters a username and password into the login form.
#2.  The username and password are sent to the server via a POST request.
#3.  The server receives the username and password.
#4.  The server connects to the database.
#5.  The server queries the database for the username and password.
#6.  The server returns a response to the user.
#
#The above code is vulnerable to SQL injection.  The username and password are not sanitized before being used in the query.  This means that an attacker can enter malicious SQL code into the username and password fields.  The malicious SQL code will be executed by the database.  The attacker can use this to bypass authentication, read data from the database, or even modify data in the database.
#
#To demonstrate this, let's try to login with the following credentials:
#
#Username: admin
#Password: ' OR 1=1 --
#

import requests

url = "http://example.com/login"

data = {
    "username": "admin",
    "password": "' OR 1=1 --"
}

r = requests.post(url, data=data)

print(r.text)


The above code will send a POST request to the login page with the username "admin" and the password "' OR 1=1 --".  The single quotes in the password will cause the SQL query to be malformed.  However, the OR 1=1 condition will always evaluate to true.  This will cause the database to return a response as if the login was successful.