
#
#1. It is taking the username and password from the request.
#2. It is connecting to the database.
#3. It is executing a query to check if the username and password are correct.
#4. It is returning the results.
#
#The problem is that the query is vulnerable to SQL injection.
#
#The query is vulnerable because it is using string concatenation to build the query.
#
#The query should be using parameterized queries.
#
#The query should look like this:
#
#query = "SELECT * FROM `users` WHERE `username`=%s AND `password`=%s"
#cursor.execute(query, (username, password))
#
#The query is now using parameterized queries.
#
#The query is now safe from SQL injection.
#
#The query is now safe from SQL injection because the username and password are being passed as parameters.
#
#The query is now safe from SQL injection because the

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM `users` WHERE `username`=%s AND `password`=%s"
val = (username, password)
mycursor.execute(sql, val)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)