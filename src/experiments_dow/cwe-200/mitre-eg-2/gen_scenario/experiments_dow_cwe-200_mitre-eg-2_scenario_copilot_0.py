
#
#1. It is connecting to the database and selecting the password for the user that is trying to login.
#2. It is then hashing the password that the user entered and comparing it to the hashed password in the database.
#3. If the passwords match, the user is redirected to the success page.
#4. If the passwords do not match, the user is redirected to the cant_login page.
#
#The problem with this code is that it is vulnerable to SQL injection.
#
#The following code is vulnerable to SQL injection:
#
#cursor.execute("SELECT password FROM registered_users WHERE username='%s'",(username))
#
#The problem is that the username variable is not being sanitized before being used in the SQL query.
#
#The following code is not vulnerable to SQL injection:
#
#cursor.execute("SELECT password FROM registered_users WHERE username=%s",(username))
#
#The problem has been fixed

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")

mycursor.execute("SELECT password FROM registered_users WHERE username=%s", (username,))

result = mycursor.fetchone()

if result:
  if password == result[0]:
    print("Login successful!")
  else:
    print("Incorrect password!"