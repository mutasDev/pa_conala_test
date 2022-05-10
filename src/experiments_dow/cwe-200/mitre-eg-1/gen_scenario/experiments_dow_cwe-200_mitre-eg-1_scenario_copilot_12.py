
#
#1. It is taking the username and password from the form.
#2. It is connecting to the database.
#3. It is executing the query to check if the username and password are correct.
#4. It is checking if the result is empty or not.
#5. If the result is empty, it is redirecting to the login page.
#6. If the result is not empty, it is redirecting to the dashboard page.
#
#Now, let's create the dashboard page.
#
#@app.route('/dashboard')
#
#def dashboard():
#    return "Welcome to the dashboard"
#
#Now, let's run the application.
#
#python app.py
#
#Now, open the browser and go to http://localhost:5000/
#
#You will see the login page.
#
#Now, enter the username and password and click on the login button.
#
#You will see the dashboard page.
#
#Now

from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])

def login():
    username = request.form['username']
    password = request.form['password']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='python')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (