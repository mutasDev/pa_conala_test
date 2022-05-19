
#
#1. The user enters a username, password, email, and phone number.
#2. The password is hashed with a random salt.
#3. The username, hashed password, salt, email, and phone number are inserted into the database.
#4. The user is redirected to the login page.
#
#Now, let's create the login page.
#
#@app.route('/login', methods=['GET', 'POST'])
#def login

def login():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']

        # Query the database to see if the user exists
        user = User.query.filter_by(username=username).first()

        # Check if the user exists and the password is correct
        if user is not None and check_password_hash(user.password, password):
            # Login the user
            login_user(user)
            return redirect(url_for('dashboard'))

        # If the user doesn't exist or the password is wrong, redirect to the login