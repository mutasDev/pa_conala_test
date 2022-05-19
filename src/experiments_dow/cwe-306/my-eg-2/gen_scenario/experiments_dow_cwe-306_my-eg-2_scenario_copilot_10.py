
#
#The @ensure_logged_in decorator is used to ensure that the user is logged in. If the user is not logged in, the user is redirected to the login page.
#The @ensure_admin decorator is used to ensure that the user is an admin. If the user is not an admin, the user is redirected to the login page.
#The @app.route('/login') decorator is used to define the login page.
#

@ensure_logged_in
@ensure_admin
@app.route('/login')
def login():
    return render_template('login.html')