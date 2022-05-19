
#
#1. The @app.route('/img') decorator is telling Flask what URL should trigger our function.
#2. The function is returning the HTML that will display the image located at plot.png.
#
#Now, if you run the app.py file and navigate to http://localhost:5000/img, you should see the image.
#
#'''
#
#@app.route('/')
#def index():
#    return '<h1>
</h1>'

@app.route('/img')
def img():
    return '<img src="plot.png">'

if __name__ == '__main__':
    app.run()