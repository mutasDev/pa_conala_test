
#
#It is checking if the target URL matches the regular expression.
#If it does, it redirects to the target URL.
#If it does not, it redirects to the root URL.
#
#The problem with this code is that it is not safe.
#
#The regular expression is not safe because it does not check for the protocol.
#
#The redirect function is not safe because it does not check for the protocol.
#
#The target URL could be:
#
#

import re

def is_safe_url(target):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3