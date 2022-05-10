
#
#1. The route decorator is used to tell Flask what URL should trigger our function.
#2. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#3. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#5. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#6. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the

@app.route('/')
def index():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/contact')
def contact():
    return 'This is the contact page'

@app.route('/faq')
def faq():
    return 'This is the FAQ page'

@app.route('/terms')
def terms():
    return 'This is the terms page'

@app.route('/privacy')
def privacy():
    return 'This is the privacy page'