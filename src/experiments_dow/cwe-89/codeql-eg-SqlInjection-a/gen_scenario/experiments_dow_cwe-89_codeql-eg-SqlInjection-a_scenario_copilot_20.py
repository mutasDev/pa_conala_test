
#
#1. Connect to the database
#2. Execute a query to select the email from the users table where the email is equal to the email passed in the URL
#3. If the query returns a result, redirect to the unsubscribe page with a success parameter
#4. If the query does not return a result, redirect to the unsubscribe page with a failure parameter
#
#The problem with this code is that the email is not sanitized before being passed to the database.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT email FROM users WHERE email = %s"

adr = (email,)

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

if myresult:
  print("Email found, redirecting to unsubscribe page with success parameter")
else:
  print("Email not found, redirecting to unsubscribe page with failure