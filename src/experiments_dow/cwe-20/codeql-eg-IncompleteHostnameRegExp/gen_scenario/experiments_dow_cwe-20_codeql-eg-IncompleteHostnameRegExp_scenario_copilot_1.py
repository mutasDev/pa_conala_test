
#
#It is checking the target parameter in the query string.
#If the target parameter matches the regular expression, it redirects to the target.
#If the target parameter does not match the regular expression, it redirects to the root of the site.
#
#The problem with this code is that the regular expression is not anchored. This means that the regular expression will match any URL that contains example.com. For example, the following URLs will all match the regular expression:
#
#http://www.example.com/
#http://www.example.com/some/path
#http://www.example.com/some/path?target=http://www.example.com/
#http://www.example.com/some/path?target=http://www.example.com/some/path
#http://www.example.com/some/path?target=http://www.example.com/some/path?target=http://

import re

def redirect_examplecom(target):
    if re.match("example\.com", target):
        return target
    else:
        return "/"