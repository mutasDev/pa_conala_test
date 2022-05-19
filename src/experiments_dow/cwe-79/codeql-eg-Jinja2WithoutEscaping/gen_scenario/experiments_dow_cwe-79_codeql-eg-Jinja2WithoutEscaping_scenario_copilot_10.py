
#
#1. Create a Flask app
#2. Create a Jinja2 environment
#3. Create a function that renders a response from the Jinja2 environment
#4. Create a route that renders a response from the Jinja2 environment
#
#The Jinja2 environment is created with the following parameters:
#
#loader: The loader parameter is used to load templates from a specific location. In this case, we are loading templates from the templates directory.
#autoescape: The

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()