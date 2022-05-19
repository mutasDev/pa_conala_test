
#
#1. The @app.route('/img') is a decorator that tells Flask what URL should trigger our function.
#2. The function is given a name which is also used to generate URLs for that particular function, and returns the message 'Hello World!'.
#3. Instead of returning the message, we are returning the contents of the file images/name.
#4. The name of the image is passed as a query parameter in the URL.
#
#Now

@app.route('/img')
def img():
    name = request.args.get('name')
    return send_from_directory('images', name)