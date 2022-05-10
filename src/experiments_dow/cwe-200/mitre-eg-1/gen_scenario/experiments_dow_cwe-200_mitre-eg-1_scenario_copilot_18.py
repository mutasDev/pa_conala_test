
#
#1. The user enters a username and password into the login form.
#2. The login form sends a POST request to the server.
#3. The server receives the POST request and extracts the username and password from the request.
#4. The server connects to the database and queries the database for the username and password.
#5. If the username and password are found in the database, the server takes the user to the home page.
#6. If the username and password are not found in the database, the server returns an error message.
#
#The code above is not complete. You need to add the following:
#
#1. A way to hash the password before it is sent to the server.
#2. A way to hash the password before it is stored in the database.
#3. A way to compare the hashed password sent by the user with the hashed password stored in the database.
#
#You can use the hashlib library

import hashlib

def hash_password(password):
    # Your code goes here

def check_password(hashed_password, user_password):
    # Your code goes here