
#
#1.  The function `info()` is called when the user visits the URL `/info`
#2.  The function `info()` gets the username, email, and ssn from the session
#3.  The function `info()` calls the function `return_info_page()` to return the HTML page
#4.  The function `return_info_page()` returns the HTML page with the username, email, and ssn
#
#Now, let's add a function to change the email address.  Add the following code to the file `app.py`:
#
#    @app.route('/change_email', methods=['GET', 'POST'])
#    def change_email():
#        if request.method == 'GET':
#            return '''<html>
#            <form action="/change_email" method="POST">
#            <input type="text" name="email"

def change_email():
    if request.method == 'GET':
        return '''<html>
        <form action="/change_email" method="POST">
        <input type="text" name="email"
            <input type="submit" value="Submit">
            </form>
            </html>'''
        elif request.method == 'POST':
            session['email'] = request.form['email']
            return redirect('/info')