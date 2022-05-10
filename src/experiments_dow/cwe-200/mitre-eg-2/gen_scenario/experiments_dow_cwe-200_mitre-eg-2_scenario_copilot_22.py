
#    1. It is connecting to the database
#    2. It is executing a query to get the password for the user
#    3. It is comparing the password entered by the user with the password in the database
#    4. If the passwords match, it is redirecting the user to the home page
#    5. If the passwords do not match, it is redirecting the user to the login page
#    6. If there is an error, it is redirecting the user to the login page
#
#@app.route('/register', methods=['POST'])
#def register():
#    username = request.form['username']
#    password = request.form['password']
#    try: 
    except: 
        return redirect(url_for('login'))