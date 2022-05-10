
#
#1. Connect to the database
#2. Create a cursor object
#3. Execute the SQL query
#4. Fetch the result
#5. Check if the password matches
#6. If it does, redirect to the index page
#7. If it doesn't, return an error message
#
#The code is pretty straightforward. The only thing you need to change is the database name, username, and password.
#
#Now, let's create the index page.
#
#@app.route('/index')
#def index():
#    return render_template('index.html')
#
#The index page is pretty simple. It just returns the index.html template.
#
#Now, let's create the index.html template.
#
#<!DOCTYPE html>
#<html>
#<head>
#    <title>Login</title>
#</head>
#<body>
#    <h1>Login</h1

def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index