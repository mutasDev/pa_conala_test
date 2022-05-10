
#
#1. It is connecting to the database.
#2. It is executing a query to select the user with the username that was passed in.
#3. If the user is not found, it returns "no user found".
#4. If the user is found, it checks the password.
#5. If the password is correct, it returns "OK".
#6. If the password is incorrect, it returns "password error".
#7. If there is an error connecting to the database, it returns "Failed to connect to MySQL".
#
#

import pymysql

db = pymysql.connect("localhost", "root", "", "test")

username = input("Enter username: ")

cursor = db.cursor()

cursor.execute("SELECT * FROM user WHERE username = %s", (username))

result = cursor.fetchone()

if result == None:
    print("No user found")
else:
    password = input("Enter password: ")
    if password == result[2]:
        print("OK")
    else:
        print("Password error")

db.close()