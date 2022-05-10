
#
#1. It is taking the username and password from the form.
#2. It is connecting to the database.
#3. It is executing a query to check if the username and password are correct.
#4. If the username and password are correct, it is setting the session variable and redirecting to the session page.
#5. If the username and password are incorrect, it is returning an error message.
#
#The above code is vulnerable to SQL injection.
#
#The following code is vulnerable to SQL injection:
#
#cursor.execute("SELECT * FROM users WHERE username='"+username+"' AND password='"+password+"'")
#
#The following code is not vulnerable to SQL injection:
#
#cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
#
#The following code is vulnerable to SQL injection:
#
#cursor.execute("SELECT * FROM users WHERE username

import mysql.connector 

conn = mysql.connector.connect(user='root', password='root', host='localhost', database='test') 
cursor = conn.cursor() 

username = input("Enter username: ") 
password = input("Enter password: ") 

cursor.execute("SELECT * FROM users WHERE username='"+username+"' AND password='"+password+"'") 

if cursor.fetchone(): 
    print("Login successful!") 
else: 
    print("Login failed.")