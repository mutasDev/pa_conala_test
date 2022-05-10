
#
#1. It is taking the username and password from the form.
#2. It is connecting to the database.
#3. It is executing a query to check if the username and password combination exists in the database.
#4. If the combination exists, it is redirecting the user to a YouTube video.
#5. If the combination does not exist, it is returning an error message.
#
#Now, let's see how we can exploit this code.
#
#Exploiting the Code
#
#The first thing we need to do is to create a new user in the database. We can do this by executing the following query:
#
#INSERT INTO users (username, password) VALUES ('admin', 'admin');
#
#Now, we can try to login with the username admin and the password admin.
#
#If we try to login with the username admin and the password admin, we will get the following error message:
#
#Wrong login and

import urllib, urllib2, cookielib, base64, re, os, sys, tempfile

def exploit():
    url = "http://target.com/login.php"
    post_data = urllib.urlencode({'username':'admin', 'password':'admin'})
    req = urllib2.Request(url, post_data)
    resp = urllib2.urlopen(req)
    print resp.read()

if __name__ == '__main__':
    exploit()

As we can see, the code is trying to login with the username admin and the password admin.
