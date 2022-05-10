
#
#It is taking the target parameter from the request and checking if it matches the regular expression.
#If it does, it redirects to the target.
#If it doesn't, it redirects to the root of the site.
#
#The regular expression is checking that the target starts with http://localhost: followed by a number and then a /.
#
#This is a very simple example of how to use regular expressions to check the input to your application.
#
#The regular expression is checking that the target starts with http://localhost: followed by a number and then a /.
#
#This is a very simple example of how to use regular expressions to check the input to your application.
#
#The regular expression is checking that the target starts with http://localhost: followed by a number and then a /.
#
#This is a very simple example of how to use regular expressions to check the input to your application.
#
#The regular expression is checking that the target

import re

def check_target(target):
    if re.match("^http://localhost:\d+/$", target):
        return True
    else:
        return False