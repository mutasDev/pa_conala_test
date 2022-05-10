
#
#1. The user enters a username and password on the login page.
#2. The login page sends a POST request to the server with the username and password.
#3. The server checks the database to see if the username and password are correct.
#4. If the username and password are correct, the server redirects the user to the home page.
#5. If the username and password are incorrect, the server redirects the user to the login page.
#
#The code above is not working. I am getting the following error:
#
#Traceback (most recent call last):
#  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 1836, in __call__
#    return self.wsgi_app(environ, start_response)
#  File "/usr/local/lib/python2.7/dist-packages/flask/app.

The code above is not working. I am getting the following error:

Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 1836, in __call__
    return self.wsgi_app(environ, start_response)
  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 1820, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python2.7/dist-packages/flask/app.