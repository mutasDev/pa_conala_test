
#
#1. The user enters a username and password.
#2. The username and password are sent to the server.
#3. The server checks if the username exists in the database.
#4. If the username exists, the server checks if the password is correct.
#5. If the password is correct, the server returns the access level of the user.
#6. The access level is used to determine what the user can do.
#
#The server is vulnerable to SQL injection.
#
#The server is vulnerable to SQL injection because the username and password are not sanitized before being used in the SQL query.
#
#The server is vulnerable to SQL injection because the username and password are not sanitized before being used in the SQL query.
#
#The server is vulnerable to SQL injection because the username and password are not sanitized before being used in the SQL query.
#
#The server is vulnerable to SQL injection because the username and password are not sanitized before being

import urllib2
import urllib
import re

username = "admin"
password = "admin"

url = "http://example.com/login.php"

values = {'username' : username,
          'password' : password }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

print the_page