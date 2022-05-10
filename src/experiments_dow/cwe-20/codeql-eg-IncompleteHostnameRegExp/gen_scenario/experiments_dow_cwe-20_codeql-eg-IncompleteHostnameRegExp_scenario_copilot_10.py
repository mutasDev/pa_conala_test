
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
#The target URL could be a data: URL.
#
#The target URL could be a javascript: URL.
#
#The target URL could be a vbscript: URL.
#
#The target URL could be a file: URL.
#
#The target URL could be a mailto: URL.
#
#The target URL could be a ftp: URL.
#
#The target URL could be a gopher: URL.
#
#The target URL could be a magnet: URL.
#
#The target URL could be a tel

import re

def redirect(target_url):
    if re.match(r'^https?://', target_url):
        return target_url
    else:
        return '/'