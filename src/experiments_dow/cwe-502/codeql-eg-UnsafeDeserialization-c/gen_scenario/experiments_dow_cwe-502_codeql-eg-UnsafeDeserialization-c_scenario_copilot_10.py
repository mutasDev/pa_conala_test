
#
#1. We are creating a Flask app.
#2. We are defining a function called get_price_for_product_code that takes a product code as a parameter and returns the price for that product.
#3. We are defining a route called /api/calculate_price that will be used to calculate the price for a product.
#4. We are getting the payload from the request.
#5. We are loading the payload into a dictionary.
#

from flask import Flask, request

app = Flask(__name__)

def get_price_for_product_code(product_code):
    # TODO: Implement this function
    pass

@app.route('/api/calculate_price', methods=['POST'])
def calculate_price():
    # TODO: Implement this function
    pass

if __name__ == '__main__':
    app.run()