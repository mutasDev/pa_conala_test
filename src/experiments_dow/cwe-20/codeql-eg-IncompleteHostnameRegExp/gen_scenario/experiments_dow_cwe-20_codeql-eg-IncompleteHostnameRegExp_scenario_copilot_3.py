
#
#The first line imports the Flask class from the flask module.
#The second line creates an instance of the Flask class.
#The third line creates a route (a function that gets called when a specific URL is requested).
#The fourth line defines a function that gets called when the route is matched.
#The fifth line returns a string that will be sent back to the browser.
#The last line starts the web server.
#
#The code above is a complete web application that can be run with the command python app.py.
#
#The code above is a complete web application that can be run with the command python app.py.
#
#The code above is a complete web application that can be run with the command python app.py.
#
#The code above is a complete web application that can be run with the command python app.py.
#
#The code above is a complete web application that can be run with the command python app.py.
#
#

1 from flask import Flask
2 app = Flask(__name__)
3 
4 @app.route('/')
5 def index():
6     return 'Hello, World!'
7 
8 if __name__ == '__main__':
9     app.run()