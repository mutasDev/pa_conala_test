
#
#The @app.route decorator is used to bind a function to a URL.
#
#The redirect_domain function is called when a user visits /redirect/<url>.
#
#The urlparse function is used to parse the URL.
#
#The hostname attribute is used to get the hostname of the URL.
#
#The redirect function is used to redirect the user to the URL.
#
#The else statement is used to return a message if the URL is not example.com.
#
#The return statement is used to return the output of the function.
#
#The app.run function is used to run the Flask application.
#
#The debug=True argument is used to enable the debugger.
#
#The host='0.0.0.0' argument is used to make the server publicly available.
#
#The port=8080 argument is used to specify the port on which the server will run.
#
#The app.run function

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/redirect/<url>')
def redirect_domain(url):
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'example.com':
        return redirect(url)
    else:
        return 'This domain is not allowed!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)