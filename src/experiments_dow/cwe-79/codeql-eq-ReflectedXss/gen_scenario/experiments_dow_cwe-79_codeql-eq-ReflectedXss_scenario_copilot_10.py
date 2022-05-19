
#
#@app.route("/")
#def index():
#    return "<p>Hello, World!</p>"
#
#@app.route("/hello/<username>")
#def hello_username(username):
#    return 'Hello %s' % escape(username)
#
#The first route is the index route. It is the default route that is called when you visit the root of the website. In this case, it will return a simple string.

def index():
    return "<p>Hello, World!</p>"

The second route is the hello_username route. It is called when you visit the /hello/<username> URL. In this case, it will return a string that includes the username that was passed in.
 Generated Python code: 

def hello_username(username):
    return 'Hello %s' % escape(username)