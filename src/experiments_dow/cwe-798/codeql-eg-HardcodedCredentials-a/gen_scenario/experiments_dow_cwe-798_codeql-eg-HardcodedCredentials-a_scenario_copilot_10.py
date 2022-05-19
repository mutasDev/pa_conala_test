
#
#1. The first line imports the Flask class from the flask module.
#2. The next line creates an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so

from flask import Flask

app = Flask(__name__)