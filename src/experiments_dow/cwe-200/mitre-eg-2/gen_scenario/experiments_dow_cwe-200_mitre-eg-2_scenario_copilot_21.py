
#
#1. The user enters a username and password into the login form.
#2. The login form sends a POST request to the /login route.
#3. The /login route calls the check_login function with the username and password.
#4. The check_login function connects to the database and executes a query.
#5. The query returns a result.
#6. The check_login function returns the result.
#7. The /login route returns the result.
#8. The user is redirected to the / route.
#
#The problem is that the check_login function is vulnerable to SQL injection.
#
#The check_login function is vulnerable to SQL injection because it uses string concatenation to build the query.
#
#The query is built using the username and password that the user entered into the login form.
#
#If the user enters a username of 'admin' and a password of 'password', the query will look like this:

query = "SELECT * FROM users WHERE username = 'admin' AND password = 'password'"

However, if the user enters a username of 'admin' and a password of "' OR '1'='1", the query will look like this:

query = "SELECT * FROM users WHERE username = 'admin' AND password = '' OR '1'='1'"

This query will return all rows from the users table, regardless of the password.

To fix this vulnerability, the check_login function should use parameterized queries.