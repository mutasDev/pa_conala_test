
#
#1. We import the Flask class from the flask module.
#2. We create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.
#3. We then use the route() decorator to tell Flask what URL should trigger our function.
#4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#5. Finally we have to run the application. We do this by calling the run()

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)