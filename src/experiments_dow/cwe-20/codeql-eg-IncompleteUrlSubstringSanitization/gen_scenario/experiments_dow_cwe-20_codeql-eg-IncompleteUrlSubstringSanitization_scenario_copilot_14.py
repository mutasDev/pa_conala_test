
#
#The @app.route('/redirect/<url>') decorator is telling Flask that any requests to the /redirect/<url> endpoint should be handled by the redirect_to function.
#
#The redirect_to function is taking the url parameter and checking the referrer header to see if it is coming from example.com. If it is, it will redirect to the url parameter. If it is not, it will return a 404 error.
#
#The url parameter is the url that you want to redirect to.
#
#The referrer header is the url that the request is coming from.
#
#The code=302 parameter is telling Flask that this is a temporary redirect.
#
#The '', 404 is telling Flask that we want to return a 404 error.
#
#The p.netloc == "" is checking to see if the referrer header is empty. This is because when you are testing locally, the referrer header will be

@app.route('/redirect/<url>')
def redirect_to(url):
    if request.referrer.startswith('http://example.com'):
        return redirect(url, code=302)
    else:
        return '', 404