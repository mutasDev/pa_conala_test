
#
#It is taking the target parameter from the request and checking if it matches the regular expression.
#If it does, it redirects to the target.
#If it doesn't, it redirects to the root of the site.
#
#The regular expression is checking to make sure that the target starts with http:// and does not contain a /.
#
#This is a very simple example, but it shows how you can use regular expressions to check the input to your application.
#
#The regular expression is checking to make sure that the target starts with http:// and does not contain a /.
#
#This is a very simple example, but it shows how you can use regular expressions to check the input to your application.
#
#The regular expression is checking to make sure that the target starts with http:// and does not contain a /.
#
#This is a very simple example, but it shows how you can use regular expressions to check the input to your application.
#

import re

def redirect_target(request, target):

if re.match("http://", target) and not "/" in target:

return redirect(target)

else:

return redirect("/")