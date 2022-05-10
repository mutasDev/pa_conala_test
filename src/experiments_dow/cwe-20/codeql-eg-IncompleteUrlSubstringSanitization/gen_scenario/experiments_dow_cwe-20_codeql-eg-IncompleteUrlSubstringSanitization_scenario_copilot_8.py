
#
#1. We import the Flask class from the flask module.
#2. We create an instance of the Flask class.
#3. We use the route() decorator to tell Flask what URL should trigger our function.
#4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
#5. We use the run() function to run the Flask application.
#
#We can run the application by using the following command:
#
#$ python app.py
#
#* Running on http://127.0.0.1:5000/
#
#We can now open http://127.0.0.1:5000/ in our browser and we should see the output of our application.
#
#We can also access the URL using curl:
#
#$ curl http://127.0.0.1:5000/
#
#Hello World!
#

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()