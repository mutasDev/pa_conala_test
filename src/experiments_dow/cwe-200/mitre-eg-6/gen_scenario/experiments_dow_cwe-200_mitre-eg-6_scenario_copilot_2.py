
#
#1.  The function info() is called when the user visits the URL /info.
#2.  The function info() gets the username, email, and ssn from the session.
#3.  The function info() returns a string containing the username, email, and ssn.
#
#The function info() is vulnerable to SQL injection.  The username, email, and ssn are not properly escaped.  This means that if the username, email, or ssn contains a single quote, the SQL query will be malformed.  For example, if the username is "admin'", the SQL query will be:
#
#SELECT * FROM users WHERE username='admin''
#
#This query will fail because the single quote in the username will cause the SQL query to be malformed.
#
#The SQL query will also fail if the username is "admin' OR 1=1 --".  This is because the SQL query will be:
#
#

def info():
    username = session.get('username')
    email = session.get('email')
    ssn = session.get('ssn')
    return '''
    <html>
    <body>
    <p>Username: {}</p>
    <p>Email: {}</p>
    <p>SSN: {}</p>
    </body>
    </html>
    '''.format(username, email, ssn)