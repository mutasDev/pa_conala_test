
#
#1. The login() function is called when the user submits the form.
#2. The username and password are retrieved from the form.
#3. A connection to the database is established.
#4. The username and password are passed to the SELECT query.
#5. The fetchone() method is used to retrieve the first row of the result.
#6. If the result is None, then the username or password is wrong.
#7. If the result is not None, then the username and password are correct.
#
#The above code is vulnerable to SQL injection.
#
#Let's see how we can exploit this vulnerability.
#
#Exploiting SQL Injection
#
#Let's assume that the username is admin and the password is admin.
#
#When we enter the username and password, the following query is executed:
#
#SELECT * from user where UserName= 'admin' and Password = 'admin'
#
#Now, let's enter

admin' OR '1'='1

for the password.

The following query is executed:

SELECT * from user where UserName= 'admin' and Password = 'admin' OR '1'='1'

Since '1'='1' is always true, the query will always return a result.

Thus, we are able to login even though we do not know the correct password.