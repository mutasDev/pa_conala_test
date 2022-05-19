
#
#1. The user enters a username, password, first name, last name, and email address.
#2. The password is hashed using SHA256.
#3. The username, hashed password, first name, last name, and email address are inserted into the database.
#4. The user is redirected to the login page.
#
#The code above is vulnerable to SQL injection. The username and password are not sanitized before being inserted into the database.
#
#

import hashlib

username = input("Enter a username: ")
password = input("Enter a password: ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email address: ")

hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

query = "INSERT INTO users (username, password, first_name, last_name, email) VALUES (%s, %s, %s, %s, %s)"

data = (username, hashed_password, first_name