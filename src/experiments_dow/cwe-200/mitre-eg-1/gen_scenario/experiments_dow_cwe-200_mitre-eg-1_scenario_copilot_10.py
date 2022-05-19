
#
#1. It is connecting to the database and creating a cursor object.
#2. It is executing a query to select all the rows from the user table where the username is equal to the username that was passed in.
#3. It is fetching the results of the query and storing them in a variable called results.
#4. It is checking to see if the results variable is empty. If it is, then the username does not exist in the database and the login has

import psycopg2

def login(username):
    conn = psycopg2.connect(dbname="mydatabase", user="myuser", password="mypassword", host="localhost")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE username=%s", (username,))
    results = cur.fetchall()
    if results == []:
        print("Username does not exist in database")
    else:
        print("Login successful!")
    conn.close()