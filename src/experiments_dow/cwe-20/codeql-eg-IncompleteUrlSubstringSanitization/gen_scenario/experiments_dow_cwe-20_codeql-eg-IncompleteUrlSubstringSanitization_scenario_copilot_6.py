
#
#The @app.route('/redirect/<url>') decorator is telling Flask that any requests to the /redirect/<url> URL should be handled by the redir() function.
#
#The redir() function is taking the url parameter and parsing it using the urlparse() function from the urllib.parse module.
#
#The parsed.netloc attribute is then checked to see if it is equal to example.com. If it is, the redirect() function is called to redirect the user to the URL. If it is not, the user is shown a Not Found message.
#
#The redirect() function is a Flask function that returns a redirect response to the given URL.
#
#The urlparse() function is a Python function that takes a URL and returns a ParseResult object.
#
#The ParseResult object has a netloc attribute that contains the domain name of the URL.
#
#The == operator is a

@app.route('/redirect/<url>')
def redir(url):
    parsed = urlparse(url)
    if parsed.netloc == 'example.com':
        return redirect(url)
    else:
        return 'Not Found', 404