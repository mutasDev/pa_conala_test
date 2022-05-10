
#
#1. The user enters a username and password on the login page.
#2. The login page sends a POST request to the /login route.
#3. The /login route takes the username and password from the POST request and queries the database for the password associated with the username.
#4. If the password in the database matches the password in the POST request, the user is redirected to the home page.
#5. If the password in the database does not match the password in the POST request, the user is redirected to an error page.
#
#The above code is vulnerable to SQL injection.
#
#The following code is vulnerable to SQL injection:
#
#cur.execute("SELECT password FROM user_info WHERE username=%s", [username])
#
#The above code is vulnerable because the username variable is not sanitized before being used in the SQL query.
#
#The following code is not vulnerable to SQL injection:
#
#cur.execute("SELECT

import mysql.connector

conn = mysql.connector.connect(user='root', password='password', host='localhost', database='database')

cur = conn.cursor()

username = input("Enter username: ")
password = input("Enter password: ")

cur.execute("SELECT password FROM user_info WHERE username=%s", [username])

result = cur.fetchone()

if result:
    if result[0] == password:
        print("Login successful!")
    else:
        print("Incorrect password!")
else:
    print("Username does not exist!")