
#
#1. We import the Flask class from the flask module.
#2. We create an instance of the Flask class.
#3. We define a route (URL) that will trigger the function.
#4. We define a function that will be called when the route is triggered.
#5. We run the app when the script is executed.
#
#The function that we defined is called a view function. It takes no arguments, and returns the message that we want to display

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()