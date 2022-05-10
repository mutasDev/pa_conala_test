
#
#1. The user enters a username and password into the login form.
#2. The username and password are sent to the server.
#3. The server checks the database to see if the username and password match.
#4. If they match, the server returns "Login Success".
#5. If they don't match, the server returns "Wrong Password".
#6. If the username doesn't exist, the server returns "Wrong Username".
#
#I want to make it so that if the user enters the correct username and password, they are redirected to a new page.
#
#I tried to do this by adding the following code to the end of the login() function:
#
#    if login_results == ():
#        return "Wrong Password"
#    for row in login_results:
#        if row[0] == hashlib.md5(password.encode()).hexdigest():
#            print(row[

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login_results = check_login(username, password)
    if login_results == ():
        return "Wrong Password"
    for row in login_results:
        if row[0] == hashlib.md5(password.encode()).hexdigest():
            print(row[0])
            print("Login Success")
            return redirect(url_for('new_page'))
        else:
            return "Wrong Password"