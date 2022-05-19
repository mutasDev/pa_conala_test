
#
#1. We are creating a Flask app.
#2. We are creating a route called /api.
#3. We are getting the payload from the URL.
#4. We are loading the payload into a blob.
#5. We are checking if the name of the blob is marker.
#6. If the name of the blob is marker, we are exiting the program.
#7. If the name of the blob is not marker, we are returning the name of

1. from flask import Flask, request
2. app = Flask(__name__)
3. 
4. @app.route('/api', methods=['GET'])
5. def get_data():
6.     payload = request.args.get('payload')
7.     blob = payload.split(',')
8.     if blob[0] == 'marker':
9.         exit()
10.     else:
11.         return blob[0]
12. 
13. if __name__ == '__main__':
14.     app.run()