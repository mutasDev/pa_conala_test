
#
#The route decorator is used to bind a function to a URL.
#The function redirect_url() is called when a user visits the URL /redirect/<url>.
#The <url> part of the URL is passed as an argument to the function.
#The urlparse() function is used to parse the URL.
#The netloc attribute of the parsed URL is used to check if the URL is from example.com.
#If the URL is from example.com, the user is redirected to the URL.
#If the URL is not from example.com, the user is not redirected.
#
#"""

@app.route('/redirect/<url>')
def redirect_url(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc == 'example.com':
        return redirect(url)
    else:
        return 'URL is not from example.com'