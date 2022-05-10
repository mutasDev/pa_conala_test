
#
#1. The function redirect_url() takes a url as an argument.
#2. The urlparse() function is used to parse the url.
#3. The urlparse() function returns a ParseResult object.
#4. The ParseResult object has a hostname attribute.
#5. If the hostname attribute is empty, then the url is a relative url.
#6. If the hostname attribute is not empty, then the url is an absolute url.
#7. If the hostname attribute is not empty, then the url is an absolute url.
#8. If the hostname attribute is not empty, then the url is an absolute url.
#9. If the hostname attribute is not empty, then the url is an absolute url.
#10. If the hostname attribute is not empty, then the url is an absolute url.
#11. If the hostname attribute is not empty, then the url is an absolute url

def redirect_url(url):
    parsed_url = urlparse(url)
    if parsed_url.hostname:
        return url
    else:
        return None