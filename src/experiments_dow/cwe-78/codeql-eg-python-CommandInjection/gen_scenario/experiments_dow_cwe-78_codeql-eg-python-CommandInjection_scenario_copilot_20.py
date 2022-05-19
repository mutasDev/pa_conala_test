
#
#1. We import the Flask class from the flask module.
#2. We create an instance of the Flask class.
#3. We use the route() decorator to tell Flask what URL should trigger our function.
#4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#5. Finally, we make the script executable and run it.
#
#

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)