
#
#1. We are importing the necessary modules.
#2. We are creating a Flask object.
#3. We are creating a route for the login page.
#4. We are getting the username and password from the form.
#5. We are connecting to the database.
#6. We are creating a cursor object.
#7. We are creating a SQL query.
#8. We are executing the query.
#9. We are fetching the results.
#10

1. import flask
2. app = flask.Flask(__name__)
3. @app.route('/login')
4. def login():
5.     username = flask.request.form['username']
6.     password = flask.request.form['password']
7.     db = flask.sqlite3.connect('database.db')
8.     cursor = db.cursor()
9.     cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
10.    results = cursor.fetchall()