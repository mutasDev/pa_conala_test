
#
#The @app.route("/") decorator tells Flask what URL should trigger our function.
#The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#
#@app.route("/hello/<username>")
#def hello(username=None):
#    return render_template("hello.html", name=username)
#
#The above code is

def hello(username=None):
    return render_template("hello.html", name=username)

The @app.route("/hello/<username>") decorator tells Flask what URL should trigger our function.
The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.