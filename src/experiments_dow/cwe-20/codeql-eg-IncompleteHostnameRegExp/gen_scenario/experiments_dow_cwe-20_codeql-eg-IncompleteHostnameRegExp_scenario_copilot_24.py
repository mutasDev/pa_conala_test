
#
#The first line imports the Flask class from the flask module.
#The second line creates an instance of the Flask class.
#The third line creates a route (a function that gets called when a specific URL is requested).
#The fourth line defines a function that gets called when the route is matched.
#The fifth line returns a string to the browser.
#The sixth line runs the application when the script is executed.
#
#The code above is a simple example of a Flask application that routes requests to the root URL (/) to the home() function.
#
#The home() function returns the string 'Hello World!'.
#
#The run() function runs the application on a local development server.
#
#The application is run on port 5000, and if you visit http://localhost:5000/ in your browser, you should see the output of the home() function, which is the string 'Hello World!'.
#
#The route() function is used to bind a function

import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()