
#
#The post() function is called when a POST request is made to the /post URL.
#The username and message are extracted from the request.
#The insert_user_message_in_db() function is called to insert the message into the database.
#The user is redirected to the / URL.
#
#@app.route('/')
#def index():
#    username = session['username']
#    messages = get_messages_from_db()
#

@app.route('/')
def index():
    username = session['username']
    messages = get_messages_from_db()
    return render_template('index.html', username=username, messages=messages)