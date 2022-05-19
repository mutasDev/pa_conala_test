
#
#1. It is connecting to the database and selecting the password for the user that is trying to login.
#2. It is then hashing the password that the user entered and comparing it to the hashed password in the database.
#3. If the passwords match, the user is redirected to the success page.
#4. If the passwords do not match, the user is redirected to the cant_login page.
#
#The problem with this code is that it is vulnerable to

1. It is connecting to the database and selecting the password for the user that is trying to login.
2. It is then hashing the password that the user entered and comparing it to the hashed password in the database.
3. If the passwords match, the user is redirected to the success page.
4. If the passwords do not match, the user is redirected to the cant_login page.

The problem with this code is that it is vulnerable to

1. SQL injection
2. Password brute forcing