
#
#1. The function redirect_url takes in a url as a parameter.
#2. The urlparse function is used to parse the url.
#3. If the url does not have a hostname, then the url is stripped of any leading or trailing slashes and then redirected.
#4. If the url has a hostname, then the url is stripped of any leading or trailing slashes and then redirected.
#5. If the url has a hostname that is

def redirect_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.hostname:
        url = url.strip('/')
        return redirect(url)
    else:
        url = url.strip('/')
        return redirect(url)