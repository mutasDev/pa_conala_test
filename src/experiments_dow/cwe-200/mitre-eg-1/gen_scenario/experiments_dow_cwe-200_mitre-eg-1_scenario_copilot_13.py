
#
#1. It is taking the username and password from the form.
#2. It is connecting to the database.
#3. It is executing the query.
#4. It is fetching the result.
#5. It is committing the changes.
#6. It is closing the connection.
#7. It is checking if the result is empty or not.
#8. If the result is empty, it is returning the message 'wrong username/password'.
#9. If the result is not empty, it is redirecting to the dashboard.
#
#Now, let's create the dashboard.
#
#@app.route('/dashboard')
#
#def dashboard():
#    return 'Welcome to the dashboard'
#
#if __name__ == '__main__':
#    app.run(debug=True)
#
#Now, let's run the application and test it.
#
#python app.py
#
#Open the browser and go to http

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mydatabase"
        )
        my