
#
#1. We are using the Flask framework to create a web server.
#2. We are using the @app.route decorator to define a route.
#3. We are using the request object to get the payload parameter from the URL.
#4. We are using the yaml.safe_load function to parse the payload parameter.
#5. We are using the get function to get the product_code and quantity from the yaml_data object.
#6

1. import flask
2. app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/<string:payload>')
def show_post(payload):
    yaml_data = yaml.safe_load(payload)
    product_code = yaml_data.get('product_code')
    quantity = yaml_data.get('quantity')
    return '''
        Product code: {}
        Quantity: {}
    '''.format(product_code, quantity)

if __name__ == '__main