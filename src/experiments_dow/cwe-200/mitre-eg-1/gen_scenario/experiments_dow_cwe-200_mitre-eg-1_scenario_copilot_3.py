
#
#1. The login() function is called when the user submits the login form.
#2. The username and password are retrieved from the form.
#3. A connection to the database is established.
#4. The username and password are retrieved from the database.
#5. The username and password are compared to the ones submitted by the user.
#6. If the username and password match, the user is redirected to the home page.
#7. If the username and password do not match, the user is redirected to the login page.
#
#The above code is vulnerable to SQL injection. The username and password are not sanitized before being used in the SQL query.
#
#The following code is vulnerable to SQL injection:
#
#cursor.execute("SELECT username, password, role FROM user")
#
#The following code is not vulnerable to SQL injection:
#
#cursor.execute("SELECT username, password, role FROM user WHERE username = %s

def login():
    username = request.form['username']
    password = request.form['password']

    connection = mysql.connector.connect(user='root', password='root',
                                         host='localhost',
                                         database='test')

    cursor = connection.cursor()
    cursor.execute("SELECT username, password, role FROM user")

    for (username, password, role) in cursor:
        if (username == request.form['username'] and 
            password == request.form['password']):
            return redirect(url_for('home'))

    return redirect(url_for('login'))