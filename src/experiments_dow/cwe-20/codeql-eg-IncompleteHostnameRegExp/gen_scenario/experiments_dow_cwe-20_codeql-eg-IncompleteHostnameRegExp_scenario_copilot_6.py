
#
#It is checking the target parameter in the query string.
#If the target parameter matches the regular expression, it redirects to the target.
#If the target parameter does not match the regular expression, it redirects to the root of the site.
#
#The problem with this code is that it is not safe.
#
#The regular expression is not anchored to the beginning of the string.
#This means that the regular expression will match any string that contains example.com.
#
#For example, the following URL will redirect to http://example.com/:
#
#http://www.example.com/some/path?target=http://www.google.com/%0Ahttp://example.com/
#
#The following URL will redirect to http://example.com/:
#
#http://www.example.com/some/path?target=http://www.google.com/%0Ahttp://example.com/%0

import re

def redirect_to_example_com(target):
    if re.search('example.com', target):
        return redirect(target)
    else:
        return redirect('/')