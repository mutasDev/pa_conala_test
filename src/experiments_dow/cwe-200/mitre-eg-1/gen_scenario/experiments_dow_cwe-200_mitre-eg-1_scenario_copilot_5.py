
#
#1. The user enters a username and password on the login page.
#2. The username and password are sent to the server.
#3. The server checks the database to see if the username exists.
#4. If the username does not exist, the server returns an error message.
#5. If the username exists, the server checks the database to see if the password matches the username.
#6. If the password does not match, the server returns an error message.
#7. If the password matches, the server returns the home page.
#
#I am having trouble with step 5. I am not sure how to check the database to see if the password matches the username. I am using the SHA512 algorithm to hash the password. I am using the following code to hash the password:
#
#hashlib.sha512(password.encode()).hexdigest()
#
#I am using the following code to check the database:
#
#

def check_password(username, password):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result == None:
        return False
    else:
        return True