
#
#1. The route decorator is used to tell Flask what URL should trigger our function.
#2. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#3. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#4. The function

@app.route('/')
def index():
    return 'Hello, World!'