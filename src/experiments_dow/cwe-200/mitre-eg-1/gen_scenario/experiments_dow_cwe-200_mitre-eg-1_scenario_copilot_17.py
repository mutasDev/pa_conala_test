
#
#1. The user enters their username and password into the login form.
#2. The login form sends a POST request to the /login route.
#3. The /login route takes the username and password from the POST request and queries the database for the user.
#4. If the user exists, the password is hashed and compared to the hashed password in the database.
#5. If the password is correct, the user is redirected to the /user route.
#6. If the password is incorrect, the user is told that their password is incorrect.
#7. If the user does not exist, the user is told that the user does not exist.
#
#The code above is a very basic login system. It is not secure and should not be used in a production environment.
#
#The code above is vulnerable to SQL injection.
#
#The code above is vulnerable to XSS.
#
#The code above is vulnerable to CSRF.
#

import hashlib

def login(username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False