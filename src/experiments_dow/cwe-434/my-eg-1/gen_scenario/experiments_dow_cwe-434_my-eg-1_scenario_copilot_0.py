
#
#1. The first line imports the Flask class. An instance of this class will be our WSGI application.
#2. The next line creates an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the

from flask import Flask 
app = Flask(__name__) 
@app.route('/') 
def index(): 
    return 'Hello World!' 
if __name__ == '__main__': 
    app.run()