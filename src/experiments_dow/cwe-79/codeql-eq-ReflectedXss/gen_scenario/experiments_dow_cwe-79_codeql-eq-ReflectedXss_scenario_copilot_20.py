
#
#@app.route("/hello/<username>")
#def hello_user(username):
#    return '<h1>Hello %s</h1>' % escape(username)
#
#The @app.route("/hello/<username>") is a decorator. It tells Flask what URL should trigger our function. In this case we want to trigger it when we go to /hello/<username> , where <username> is a variable

def hello_user(username):
    return '<h1>Hello %s</h1>' % escape(username)

@app.route("/hello/<username>")
def hello_user(username):
    return '<h1>Hello %s</h1>' % escape(username)