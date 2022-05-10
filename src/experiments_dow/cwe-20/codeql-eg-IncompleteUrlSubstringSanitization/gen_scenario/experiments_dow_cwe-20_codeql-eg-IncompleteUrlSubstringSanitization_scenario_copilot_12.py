
#
#The @app.route decorator is used to bind a function to a URL.
#
#The function redirectto() is called when a user visits /redirect/<url>
#
#The url variable is passed to the function.
#
#The urlparse() function is used to parse the url variable.
#
#The netloc attribute is used to get the domain name of the URL.
#
#If the domain name is example.com, the user is redirected to the URL.
#
#If the domain name is not example.com, the user is shown a 404 error.
#
#The redirect() function is used to redirect the user to the URL.
#
#The return statement is used to return the output to the user.
#
#The return statement is used to return the output to the user.
#
#The return statement is used to return the output to the user.
#
#The return statement is used to return the output to the user.
#
#

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/redirect/<url>')
def redirectto(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain == 'example.com':
        return redirect(url_for('url'))
    else:
        return abort(404)