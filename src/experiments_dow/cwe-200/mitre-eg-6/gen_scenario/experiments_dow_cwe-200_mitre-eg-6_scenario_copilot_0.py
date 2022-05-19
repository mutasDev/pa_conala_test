
#
#1.  The function `info()` is called when the user visits the URL `/info`
#2.  The function `info()` gets the username, email, and ssn from the session
#3.  The function `info()` calls the function `return_info_page()` to return the HTML page
#4.  The function `return_info_page()` returns the HTML page with the username, email, and ssn
#

def info():
    username = session.get('username')
    email = session.get('email')
    ssn = session.get('ssn')
    return return_info_page(username, email, ssn)

def return_info_page(username, email, ssn):
    return '''
    <html>
    <body>
    <p>Username: {}</p>
    <p>Email: {}</p>
    <p>SSN: {}</p>
    </body>
    </html>
    '''.format(username, email, ssn)