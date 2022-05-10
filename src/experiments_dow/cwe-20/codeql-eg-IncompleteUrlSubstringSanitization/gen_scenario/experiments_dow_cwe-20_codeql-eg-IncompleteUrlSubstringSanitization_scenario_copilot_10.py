
#
#1. The function redirect_url takes a url as a parameter.
#2. The function then checks to see if the url parameter is not None.
#3. If the url parameter is not None, the function parses the url using the urlparse function.
#4. The function then checks to see if the parsed url's netloc is equal to "example.com".
#5. If the parsed url's netloc is equal to "example.com", the function redirects the user to the parsed url's netloc and path.
#6. If the parsed url's netloc is not equal to "example.com", the function returns a 404 error.
#7. If the url parameter is None, the function returns a 404 error.
#
#

def redirect_url(url):
    if url is not None:
        parsed_url = urlparse(url)
        if parsed_url.netloc == "example.com":
            return redirect(parsed_url.netloc + parsed_url.path)
        else:
            return abort(404)
    else:
        return abort(404)