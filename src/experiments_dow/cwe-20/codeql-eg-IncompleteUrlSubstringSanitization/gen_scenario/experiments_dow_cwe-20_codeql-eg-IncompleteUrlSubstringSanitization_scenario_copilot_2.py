
#
#1. We import the Flask class from the flask module.
#2. We create an instance of the Flask class.
#3. We use the route() decorator to tell Flask what URL should trigger our function.
#4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#5. We use the run() function to run the Flask application. We pass it the host and port, so that Flask can run on the external IP and port.
#6. We set the debug to True, so that the server will reload itself on code changes.
#7. We run the app on port 5000 on all available interfaces.
#
#'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)