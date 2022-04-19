#Flask set folder 'wherever' as the default template folder


from flask import Flask app = Flask(__name__, template_folder='wherever')