
#
#1. It is taking the username and password from the request.
#2. It is hashing the password using md5.
#3. It is inserting the username and password into the database.
#
#Now, let's see what happens when we try to register a user with the username 'admin' and password 'admin'.
#
#The query that is executed is:
#
#INSERT INTO users VALUES('admin','21232f297a57a5a7438

import hashlib

password = input("Please enter a password: ")

hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()

print("The hashed password is: " + hashed_password)