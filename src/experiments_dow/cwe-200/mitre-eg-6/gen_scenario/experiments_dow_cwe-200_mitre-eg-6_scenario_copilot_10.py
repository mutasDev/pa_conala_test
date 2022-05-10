
#
#1.  The function return_info_page() returns a string that contains the username, email, and last 4 digits of the SSN.
#2.  The function info() is called when the user visits the /info page.
#3.  The function info() gets the username, email, and last 4 digits of the SSN from the session.
#4.  The function info() calls return_info_page() to get the HTML page.
#5.  The function info() returns the HTML page.
#
#The code above is vulnerable to XSS.  The username, email, and last 4 digits of the SSN are not escaped.  This means that if the username, email, or last 4 digits of the SSN contain HTML, the HTML will be rendered.  This means that if the username, email, or last 4 digits of the SSN contain JavaScript, the JavaScript will be executed.
#
#The code above

def return_info_page(username, email, ssn):
    return '''
    <html>
    <body>
    Username: %s<br>
    Email: %s<br>
    Last 4 digits of SSN: %s<br>
    </body>
    </html>
    ''' % (username, email, ssn)

def info():
    username = session.get('username')
    email = session.get('email')
    ssn = session.get('ssn')
    return return_info_page(username, email, ssn)