
#
#1.  The function `info()` is called when the user visits the URL `/info`.
#2.  The function `info()` gets the username, email, and ssn from the session.
#3.  The function `info()` calls the function `return_info_page()` to return the HTML page.
#
#The function `return_info_page()` is defined as follows:
#
#```
#def return_info_page(username, email, ssn_last_4):
#    return "<html>Username:" + username + "<br>Email:"+email+"<br>SSN (last 4 digits):"+ssn_last_4+"</html>"
#```
#
#The function `return_info_page()` takes three parameters: `username`, `email`, and `ssn_last_4`. It returns an HTML page that displays the

```
def info():
    username = session.get('username')
    email = session.get('email')
    ssn_last_4 = session.get('ssn_last_4')
    return return_info_page(username, email, ssn_last_4)
```