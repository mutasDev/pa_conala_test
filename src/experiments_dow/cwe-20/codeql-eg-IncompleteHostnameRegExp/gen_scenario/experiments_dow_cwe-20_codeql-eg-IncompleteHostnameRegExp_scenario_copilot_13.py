
#
#The first line imports the Flask class from the flask module.
#The second line creates an instance of the Flask class.
#The third line creates a route (a function that gets called when a specific URL is requested).
#The fourth line defines a function that gets called when the route is matched.
#The fifth line returns a string that will be sent back to the browser.
#The last line starts the web server.
#
#The code above is a simple HTTP server that responds to every request with the text "Hello World".
#
#The route() decorator tells Flask what URL should trigger our function. In this case, we are telling Flask to trigger our function when the URL path is /.
#
#The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#
#The last line of the code block simply starts the web server.
#
#The web

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run()