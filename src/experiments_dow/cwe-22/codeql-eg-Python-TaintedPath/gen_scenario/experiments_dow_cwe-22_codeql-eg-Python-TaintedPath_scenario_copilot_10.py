
#
#1. The @app.route('/img') decorator is telling Flask what URL should trigger our function.
#2. The function is returning a string that is the path to the image file.
#3. The request.args.get('f','1.jpg') part is Flask specific. It is saying:
#    a. Look in the URL for a variable named f.
#    b. If it exists, use it.
#    c. If it

@app.route('/img')
def get_image():
    return 'static/' + request.args.get('f','1.jpg')