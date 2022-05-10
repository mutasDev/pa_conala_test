
#
#1.  The function info() is called when the user visits the URL /info.
#2.  The function info() gets the username, email, and ssn from the session.
#3.  The function info() calls return_info_page() to generate the HTML page.
#4.  The function return_info_page() returns the HTML page.
#5.  The function info() returns the HTML page.
#6.  The user sees the HTML page.
#
#

def info():
    username = session.get('username')
    email = session.get('email')
    ssn = session.get('ssn')
    return return_info_page(username, email, ssn)

def return_info_page(username, email, ssn):
    html = '''
    <html>
    <head>
    <title>Info Page</title>
    </head>
    <body>
    <h1>Info Page</h1>
    <p>Username: %s</p>
    <p>Email: %s</p>
    <p>SSN: %