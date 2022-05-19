
#
#1. We are creating a Flask app.
#2. We are creating a function called get_price_for_product_code that takes a product code as a parameter and returns the price of the product.
#3. We are creating a route called /api/calculate_price that takes a payload parameter.
#4. We are deserializing the payload parameter into a dict.
#5. We are getting the product code and quantity from the dict.
#

from flask import Flask, request

app = Flask(__name__)

@app.route('/api/calculate_price', methods=['POST'])
def calculate_price():
    payload = request.get_json()
    product_code = payload['product_code']
    quantity = payload['quantity']

    price = get_price_for_product_code(product_code)
    total_price = price * quantity

    return {'total_price': total_price}

def get_price_for_product_code(product_code):
    # TODO: get price from database
    return 10.0