
#
#1. The function redirect_url takes a url as a parameter.
#2. The function then checks to see if the url parameter is not None.
#3. If the url parameter is not None, the function parses the url using the urlparse function.
#4. The function then checks to see if the parsed url's netloc is equal to "example.com".
#5. If the parsed url's netloc is equal to "example.com", the

def redirect_url(url):
    if url is not None:
        parsed_url = urlparse(url)
        if parsed_url.netloc == "example.com":
            return parsed_url.scheme + "://" + parsed_url.netloc + "/" + parsed_url.path
    return None