
#
#It is checking if the target parameter is a valid domain name.
#If it is, it redirects to the target.
#If it is not, it redirects to the root of the site.
#
#The problem is that the regular expression is not correct.
#
#The regular expression should match any domain name that ends with .example.com.
#
#The regular expression should not match any domain name that ends with .example.com followed by a slash.
#
#The regular expression should not match any domain name that ends with .example.com followed by a colon and a port number.
#
#The regular expression should not match any domain name that ends with .example.com followed by a slash and a path.
#
#The regular expression should not match any domain name that ends with .example.com followed by a question mark and a query string.
#
#The regular expression should not match any domain name that ends with .example.com followed by a

import re

def check_target(target):
    if re.match("^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.example\.com$", target):
        return True
    else:
        return False