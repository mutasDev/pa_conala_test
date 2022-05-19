
#
#1. The @app.route('/url/ping') decorator is used to tell Flask what URL should trigger our function.
#2. The function ping() is called when the user visits the URL http://localhost:5000/url/ping.
#3. The URL to ping is stored as a variable "url".
#4. The ping command is run using the system command "ping".
#5. The output of the ping command is returned to the user.

@app.route('/url/ping')
def ping():
    url = request.args.get('url')
    output = subprocess.check_output(["ping", "-c", "4", url])
    return output