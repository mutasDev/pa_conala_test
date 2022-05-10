
#
#1. It is connecting to the database and creating a cursor object.
#2. It is executing a query to select all the rows from the user table where the username is equal to the username that was passed in.
#3. It is fetching the results of the query and storing them in a variable called results.
#4. It is checking to see if the results variable is empty. If it is, then the username does not exist in the database and the login has failed.
#5. If the results variable is not empty, then it is getting the hashed password from the first row of the results variable.
#6. It is comparing the hashed password from the database to the hashed password of the password that was passed in. If they are equal, then the login has succeeded.
#7. If the login has succeeded, it is returning a welcome message.
#8. If the login has failed, it is returning a login failed message.

def login(username, password):
    cursor = database.cursor()
    cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
    results = cursor.fetchall()
    if not results:
        return "Login failed"
    else:
        hashed_password = results[0]["hashed_password"]
        if hashed_password == password:
            return "Welcome!"
        else:
            return "Login failed"