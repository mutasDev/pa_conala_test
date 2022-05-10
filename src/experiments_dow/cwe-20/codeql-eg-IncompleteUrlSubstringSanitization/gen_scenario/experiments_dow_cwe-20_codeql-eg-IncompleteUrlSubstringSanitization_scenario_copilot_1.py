
#
#The @app.route decorator is used to tell Flask what URL should trigger our function.
#The function redirect_from_url takes one argument, url, which is bound to the URL argument passed to the function.
#The urlparse function from the urllib.parse module is used to parse the URL.
#The netloc attribute of the parsed URL is checked to see if it is example.com.
#If it is, the redirect function is used to redirect the user to the URL.
#If it is not, a 400 error is returned to the user.
#
#The redirect function is used to redirect the user to a different URL. The code argument is used to specify the HTTP status code. In this case, we use a 302 status code, which indicates that the resource has temporarily moved.
#
#The redirect function is used to redirect the user to a different URL. The code argument is used to specify the HTTP status code. In this case

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'secret':
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')