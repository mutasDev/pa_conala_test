
#
#1. We are creating a Flask app.
#2. We are creating a route called /api.
#3. We are getting the payload from the URL.
#4. We are loading the payload into a dictionary.
#5. We are checking if the name key is in the dictionary.
#6. If the name key is in the dictionary, we are returning the value of the name key.
#7. If the name key is not in the dictionary, we are

from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    payload = request.args
    data = payload.to_dict()
    if 'name' in data:
        return data['name']
    else:
        return 'No name key found'