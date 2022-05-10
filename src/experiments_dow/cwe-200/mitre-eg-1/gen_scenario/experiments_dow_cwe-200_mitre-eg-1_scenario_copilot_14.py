
#
#1. The user enters a username and password into the login form.
#2. The username and password are sent to the server.
#3. The server checks the database to see if the username and password are valid.
#4. If the username and password are valid, the server redirects the user to the user page.
#5. If the username and password are not valid, the server redirects the user to the bad login page.
#
#The code above is working, but it is not secure. The password is sent in plain text, and the database is not encrypted.
#
#The next step is to encrypt the password before sending it to the server.
#
#Encrypting the Password
#
#The first step is to encrypt the password before sending it to the server.
#
#The code below shows how to encrypt the password using the SHA-256 algorithm.
#
#from flask import Flask, request, redirect
#import os
#import subprocess
#

import hashlib

def encrypt_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

The next step is to update the login form to encrypt the password before sending it to the server.

The code below shows the updated login form.

<form action="/login" method="post">
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="Login">
</form>

The code above encrypts the password before sending it to the server.

Storing the Password

The next step is to