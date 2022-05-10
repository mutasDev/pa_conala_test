
#
#1.  The function `info()` is called when the user visits the URL `/info`.
#2.  The function `info()` gets the username, email, and SSN from the session.
#3.  The function `info()` prints the username, email, and SSN to the console.
#4.  The function `info()` returns a page that displays the username, email, and SSN.
#
#The function `return_info_page()` is a helper function that returns a page that displays the username, email, and SSN.
#
#The function `info()` is vulnerable to a session fixation attack.
#
#

```python
def info():
    username = session.get('username')
    email = session.get('email')
    ssn = session.get('ssn')
    print(username, email, ssn)
    return return_info_page(username, email, ssn)
```