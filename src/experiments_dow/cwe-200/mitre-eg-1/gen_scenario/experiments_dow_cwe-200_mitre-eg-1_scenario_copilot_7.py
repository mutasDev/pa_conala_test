
#
#1. The user enters their username and password into the login form.
#2. The login form sends a POST request to the /login route.
#3. The /login route takes the username and password from the POST request and queries the database for the password hash associated with the username.
#4. The /login route then compares the password hash from the database with the hash of the password entered by the user.
#5. If the hashes match, the user is redirected to the main page.
#6. If the hashes do not match, the user is told that their username or password is incorrect.
#
#The above code is vulnerable to SQL injection.
#
#The following code is vulnerable to SQL injection:
#
#cursor.execute("SELECT password FROM user WHERE username = '" + username + "';")
#
#The above code is vulnerable to SQL injection because the username variable is not sanitized before being used in the SQL query.
#
#The

import hashlib

def login(username, password):
    cursor.execute("SELECT password FROM user WHERE username = '" + username + "';")
    password_hash = cursor.fetchone()[0]
    if password_hash == hashlib.sha256(password).hexdigest():
        return True
    else:
        return False