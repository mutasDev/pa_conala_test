
#
#1. The user enters their username and password into the login form.
#2. The login form sends a POST request to the /login route.
#3. The /login route takes the username and password from the POST request and stores them in variables.
#4. The /login route connects to the database and selects the password for the user with the username that was entered.
#5. The /login route hashes the password that was entered and compares it to the hashed password that was retrieved from the database.
#6. If the passwords match, the /login route creates a session ID and stores it in the database.
#7. The /login route sets a cookie with the session ID and the username.
#8. The /login route redirects the user to the home page.
#
#Now that we have a way to log in users, we need to make sure that only logged in users can access the /admin route. We can do this by

1. Checking if the user is logged in when they try to access the /admin route.
2. If the user is logged in, allowing them to access the /admin route.
3. If the user is not logged in, redirecting them to the /login route.