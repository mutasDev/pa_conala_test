
#
#The first line imports the Flask class from the flask module.
#The second line creates an instance of the Flask class.
#The third line defines a route (a URL) that will be handled by the function safe.
#The fourth line defines the function safe.
#The fifth line gets the target parameter from the request.
#The sixth line checks if the target parameter matches the regular expression.
#The seventh line redirects to the target if it matches the regular expression.
#The eighth line redirects to the root URL if the target parameter does not match the regular expression.
#
#The regular expression is defined in the third line. It matches any string that contains a dot followed by zero to three characters followed by example.com.
#
#The regular expression is compiled in the first line. This is done to improve performance.
#
#The regular expression is used in the sixth line. The match method is used to check if the target parameter matches the regular expression.
#
#

import re

regex = re.compile(r'\.?\d{0,3}\.example\.com')

@app.route('/<target>')
def safe(target):
    if regex.match(target):
        return redirect(target)
    else:
        return redirect('/')