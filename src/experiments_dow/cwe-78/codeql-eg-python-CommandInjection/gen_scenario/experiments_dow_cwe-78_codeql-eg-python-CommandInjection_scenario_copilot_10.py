
#
#1. The @app.route('/url/ping') decorator is used to bind a function to a URL.
#2. The function ping() is called when the URL is visited.
#3. The URL to ping is stored as a variable "url".
#4. The ping command is run using the system command "ping".
#5. The result of the ping command is returned as "response".
#
#Now, let's run the code and see what

import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    response = os.system("ping -c 1 " + url)
    return render_template('ping.html', response=response, url=url)

if __name__ == '__main__':
    app.run()