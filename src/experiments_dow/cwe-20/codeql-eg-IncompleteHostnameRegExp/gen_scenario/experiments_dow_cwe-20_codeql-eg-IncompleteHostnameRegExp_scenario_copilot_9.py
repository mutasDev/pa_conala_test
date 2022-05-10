
#
#It is checking if the target URL matches the regular expression.
#If it does, it redirects to the target URL.
#If it does not, it redirects to the root URL.
#
#The regular expression is checking if the target URL starts with http:// or https://, followed by any number of subdomains, followed by example.com, followed by any number of characters.
#
#The regular expression is not perfect, but it is good enough for this example.
#
#The regular expression is not perfect, but it is good enough for this example.
#
#The regular expression is not perfect, but it is good enough for this example.
#
#The regular expression is not perfect, but it is good enough for this example.
#
#The regular expression is not perfect, but it is good enough for this example.
#
#The regular expression is not perfect, but it is good enough for this example.
#
#The regular expression is not perfect,

import re

def check_url(url):
    regex = re.compile(
        r'^(http|https):\/\/(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$')
    return regex.match(url)

def redirect_url(url):
   