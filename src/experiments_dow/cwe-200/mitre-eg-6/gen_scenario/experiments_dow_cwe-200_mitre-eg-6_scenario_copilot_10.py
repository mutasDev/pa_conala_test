
#
#1.  The function return_info_page() returns a string that contains the username, email, and last 4 digits of the SSN.
#2.  The function info() is called when the user visits the /info page.
#3.  The function info() gets the username, email, and last 4 digits of the SSN from the session.
#4.  The function info() calls return_info_page() to get the HTML page.
#

def return_info_page(username, email, last_4_digits_of_ssn):
    return '''
    <html>
    <head>
    <title>Info Page</title>
    </head>
    <body>
    <h1>Info Page</h1>
    <p>
    Username: %s<br>
    Email: %s<br>
    Last 4 digits of SSN: %s
    </p>
    </body>
    </html>
    ''' % (username, email, last_4_digits_of_ssn)

def info():
    username