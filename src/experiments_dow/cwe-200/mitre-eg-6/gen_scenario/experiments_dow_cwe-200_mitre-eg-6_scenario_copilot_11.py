
#
#1.  The user is redirected to the login page.
#2.  The user enters their username and password.
#3.  The login page sends a POST request to the server with the username and password.
#4.  The server checks the username and password against the database.
#5.  If the username and password are correct, the server returns a session cookie to the user.
#6.  The user is redirected to the info page.
#7.  The info page sends a GET request to the server.
#8.  The server checks the session cookie.
#9.  If the session cookie is valid, the server returns the user's information.
#
#The problem is that the session cookie is not secure.  The session cookie is just a string of characters.  The server does not encrypt the session cookie.  The server does not sign the session cookie.  The server does not check the IP address of the user. 

import requests

def login(username, password):
    login_url = 'http://example.com/login'
    data = {'username': username, 'password': password}
    response = requests.post(login_url, data=data)
    return response.cookies['session_cookie']

def get_info(session_cookie):
    info_url = 'http://example.com/info'
    cookies = {'session_cookie': session_cookie}
    response = requests.get(info_url, cookies=cookies)
    return response.text