
#
#The @app.route decorator is used to bind a function to a URL.
#
#The function redirect_me() takes a url parameter.
#
#The urlparse() function is used to parse the url parameter.
#
#The netloc attribute of the urlparse() function is used to get the domain name of the url.
#
#If the domain name is example.com, then the url is redirected to the url.
#
#If the domain name is not example.com, then the url is redirected to the home page.
#
#The code attribute of the redirect() function is used to set the HTTP status code.
#
#The default value of the code attribute is 302.
#
#The code 302 is used to indicate that the resource has been temporarily moved to a different URL.
#
#The code 301 is used to indicate that the resource has been permanently moved to a different URL.
#
#The code 307 is used to indicate that the resource has been

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/login')
def login():
    return 'login page'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

@app.route('/about')
def about():
    return 'The about page'

@app.route('/redirect/')
def redirect_me():
    url = 'http://example.com'
    return