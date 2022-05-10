
#
#1. The user enters a username and password.
#2. The username and password are sent to the server.
#3. The server checks the database to see if the username and password are correct.
#4. If the username and password are correct, the server sends the user to the home page.
#5. If the username and password are incorrect, the server sends the user back to the login page.
#
#The code above is not complete. You need to add the following:
#
#1. A way to check if the user is logged in.
#2. A way to log the user out.
#3. A way to create a new user.
#4. A way to change the user's password.
#5. A way to delete the user.
#
#You can use the code above as a starting point.
#
#You can use the following code to create a new user:
#
#cursor.execute("INSERT INTO user

def create_user(username, password):
    cursor.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
    connection.commit()

You can use the following code to change the user's password:

cursor.execute("UPDATE user SET password=? WHERE username=?", (new_password, username))
connection.commit()

You can use the following code to delete the user:

cursor.execute("DELETE FROM user WHERE username=?", (username,))
connection.commit()