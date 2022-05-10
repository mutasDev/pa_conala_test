
#
#1. It is taking the username and password from the form.
#2. It is connecting to the database.
#3. It is selecting the user from the database.
#4. It is checking if the username and password are correct.
#5. It is returning True or False.
#
#Now, we need to create a new file called login.html. This file will contain the login form.
#
#<html>
#<head>
#<title>Login</title>
#</head>
#<body>
#<form action="http://localhost:5000/login" method="post">
#<input type="text" name="username" placeholder="Username" />
#<input type="password" name="password" placeholder="Password" />
#<input type="submit" value="Login" />
#</form>
#</body>
#</html>
#
#Now, we need to create a new file called login.html

@app.route('/login', methods=['POST'])
def login():
    # Get the username and password from the form.
    username = request.form['username']
    password = request.form['password']

    # Connect to the database.
    db = get_db()

    # Select the user from the database.
    cur = db.execute('select * from users where username = ? and password = ?', [username, password])

    # Fetch one row from the database.
    user = cur.fetchone()

    # Check if the username and password are correct.
    if user is not None:
        # Login successful.