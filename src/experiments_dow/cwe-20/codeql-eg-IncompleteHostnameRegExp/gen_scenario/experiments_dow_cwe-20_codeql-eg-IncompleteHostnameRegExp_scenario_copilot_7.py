
#
#The first line creates a regular expression object that matches the following:
#
#A string that starts with http:// or https://
#Followed by an optional www.
#Followed by example.com
#Followed by an optional port number
#The second line is a route that takes a target parameter.
#
#The third line checks if the target parameter matches the regular expression.
#
#The fourth line redirects to the target if it matches.
#
#The fifth line redirects to the root if it doesn't match.
#
#The regular expression is a bit more complicated than it needs to be, but it's a good example of how to use regular expressions to validate user input.
#
#The regular expression is a bit more complicated than it needs to be, but it's a good example of how to use regular expressions to validate user input.
#
#The regular expression is a bit more complicated than it needs to be, but it's a good example of how to

import re

url_regex = re.compile(
    r'^(http://|https://)?(www\.)?example\.com(:\d{2,5})?$')

@app.route('/<target>')
def redirect_to_target(target):
    if url_regex.match(target):
        return redirect(target)
    else:
        return redirect('/')