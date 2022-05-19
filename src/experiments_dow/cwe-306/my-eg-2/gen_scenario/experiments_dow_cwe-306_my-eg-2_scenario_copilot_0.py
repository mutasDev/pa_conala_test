
#
#The @ensure_logged_in decorator is a function that takes another function as input and returns a modified version of that function. The modified version of the function checks if the user is logged in and redirects to the login page if they are not.
#
#The @app.route('/user') decorator is a function that takes another function as input and returns a modified version of that function. The modified version of the function checks if the user is logged

@ensure_logged_in
@app.route('/user')
def user_page():
    return render_template('user.html')