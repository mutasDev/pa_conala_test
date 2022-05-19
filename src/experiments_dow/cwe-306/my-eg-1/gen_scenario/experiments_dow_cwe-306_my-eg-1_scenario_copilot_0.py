
#
#The @ensure_logged_in decorator is a wrapper around the settings() function.
#The wrapper checks if the user is logged in. If they are, it lets them proceed normally.
#If they are not, it redirects them to the login page.
#The login page has a form that POSTs to /login.
#The /login route checks the username and password. If they are correct, it sets the username in the session and redirects to

def ensure_logged_in(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/login')
    return wrapper

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # check the username and password against the database
        if correct_username_and_password(username, password):
            session['username