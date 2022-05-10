
#
#The @app.route decorator is used to bind a function to a URL.
#
#The redirect_invalid_url function is called when a user visits the /redirect/<url> URL.
#
#The urlparse function is used to parse the URL.
#
#The netloc attribute of the parsed URL is used to check if the URL is from example.com.
#
#If the URL is from example.com, the redirect function is used to redirect the user to the URL.
#
#If the URL is not from example.com, the user is shown an error message.
#
#The redirect function is used to redirect the user to the URL.
#
#The user is shown an error message.
#
#The redirect function is used to redirect the user to the URL.
#
#The user is shown an error message.
#
#The redirect function is used to redirect the user to the URL.
#
#The user is shown an error message

@app.route('/redirect/<url>')
def redirect_invalid_url(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc != 'example.com':
        return redirect(url_for('error'))
    else:
        return redirect(url)

@app.route('/error')
def error():
    return 'Error: Invalid URL'