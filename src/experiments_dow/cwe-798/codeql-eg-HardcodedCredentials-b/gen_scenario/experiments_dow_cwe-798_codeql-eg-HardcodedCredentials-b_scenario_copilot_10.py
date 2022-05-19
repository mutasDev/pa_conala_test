
#
#1. We are importing the Flask class from the flask module.
#2. We are creating an instance of the Flask class.
#3. We are defining a route (or URL) that will trigger the function.
#4. We are defining a function that will be called when the route is triggered.
#5. We are returning a string that will be displayed on the web page.
#
#Now, let's run the application.
#
#$ python app.py
#

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    