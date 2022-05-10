
#
#1. It is creating a new Flask application called app.
#2. It is defining a function called return_info_page that takes three arguments: username, email, and ssn_last_4. This function returns a string that contains the username, email, and last four digits of the SSN.
#3. It is defining a route called /info that will respond to GET requests.
#4. It is defining a function called info that will be called when a GET request is sent to /info. This function will return a redirect to /info/username/email/ssn_last_4.
#
#

from flask import Flask, redirect

app = Flask(__name__)

@app.route('/info')
def info():
    return redirect('/info/username/email/ssn_last_4')

def return_info_page(username, email, ssn_last_4):
    return username + ' ' + email + ' ' + ssn_last_4

if __name__ == '__main__':
    app.run()