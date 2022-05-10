
#
#1.  The function `info()` is called when the user visits the URL `/info`
#2.  The function `info()` gets the username, email, and ssn from the session
#3.  The function `info()` calls the function `return_info_page()` to return the HTML page
#4.  The function `return_info_page()` returns the HTML page with the username, email, and ssn
#
#Now, let's look at the code for the function `return_info_page()`:
#
#    def return_info_page(username, email, ssn_last_4):
#        return "<html>Username:" + username + "<br>Email:"+email+"<br>SSN (last 4 digits):"+ssn_last_4+"</html>"
#
#

```python
def return_info_page(username, email, ssn_last_4):
    return "<html>Username:" + username + "<br>Email:"+email+"<br>SSN (last 4 digits):"+ssn_last_4+"</html>"
```



Now, let's look at the code for the function `return_info_page()`:

    def return_info_page(username, email, ssn_last_4):
        return "<html>Username:" + username + "<br>Email:"+email+"<br>SSN (last 4 digits):"+ssn_last