
#
#The redirect_view function is a view function that takes a URL as a parameter.
#The urlparse function is used to parse the URL.
#The urlparse function returns a ParseResult object.
#The ParseResult object has a scheme, netloc, and path attribute.
#The scheme attribute is the protocol of the URL.
#The netloc attribute is the domain name of the URL.
#The path attribute is the path of the URL.
#The if statement checks if the scheme, netloc, and netloc are valid.
#If the URL is valid, the redirect function is used to redirect the user to the URL.
#If the URL is not valid, the user is not redirected.
#
#The redirect function is used to redirect the user to a different URL.
#The redirect function takes a URL as a parameter.
#The redirect function returns a redirect response to the URL.
#The redirect response has a status code of 302.
#The

def redirect_view(url):
    parsed = urlparse(url)
    if parsed.scheme and parsed.netloc and parsed.path:
        return redirect(url)
    else:
        return HttpResponse("Invalid URL")