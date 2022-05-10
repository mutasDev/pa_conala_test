
#
#1. It is taking the username and password from the form.
#2. It is connecting to the database.
#3. It is checking if the username exists in the database.
#4. If the username exists, it is checking if the password is correct.
#5. If the password is correct, it is redirecting to the success page.
#6. If the password is incorrect, it is redirecting to the wrong page.
#7. If the username does not exist, it is redirecting to the wrong page.
#
#Now, let's create the success page.
#
#Create a file called success.html and add the following code to it:
#
#<html>
#<head>
#<title>Success</title>
#</head>
#<body>
#<h1>Success</h1>
#</body>
#</html>
#
#Now, let's create the wrong page.
#
#Create a file called

#!/usr/bin/python
import cgi, cgitb 
import mysql.connector

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('username')
password = form.getvalue('password')

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

# Execute SQL select statement
cursor = db.cursor()
sql = "SELECT * FROM users WHERE username = '%s'" % \
(username