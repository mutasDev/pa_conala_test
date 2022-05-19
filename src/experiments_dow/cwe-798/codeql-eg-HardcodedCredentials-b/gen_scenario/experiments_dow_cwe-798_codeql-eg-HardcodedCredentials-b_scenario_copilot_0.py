
#
#1. It is creating a Flask app.
#2. It is defining a route called /check_mod.
#3. It is defining a function called check_mod.
#4. It is getting the username and password from the URL.
#5. It is connecting to the database.
#6. It is executing a query to check if the username and password are correct.
#7. It is returning True or False based on the result of the query.
#
#

import flask

app = flask.Flask(__name__)

@app.route('/check_mod')
def check_mod():
    username = flask.request.args.get('username')
    password = flask.request.args.get('password')

    db = flask.sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    result = cursor.fetchone()

    if result:
        return 'True'
    else:
        return 'False'