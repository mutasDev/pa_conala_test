
#
#1. It is taking the username and password from the form.
#2. It is hashing the password using the md5 algorithm.
#3. It is storing the username and password in the database.
#4. It is redirecting the user to the home page.
#
#Now, let's create the login page.
#
#@app.route('/login', methods=['POST'])
#
#def login():
#   username = request.form['username']

def login():
   username = request.form['username']
   password = request.form['password']
   db = get_db()
   error = None

if not username:
   error = 'Username is required.'
elif not password:
   error = 'Password is required.'
else:
   db = get_db()
   error = None

user = db.execute(
   'SELECT * FROM user WHERE username = ?', (username,)
).fetchone()

if user is None:
   error = 'Incorrect username.'
elif not check_password_hash(user['password'], password):
   error =