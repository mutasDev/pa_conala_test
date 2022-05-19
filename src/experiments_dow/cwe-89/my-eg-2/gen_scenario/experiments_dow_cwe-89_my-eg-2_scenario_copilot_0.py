
#
#It is creating a route called /post.
#It is accepting only POST requests.
#It is getting the username and message from the request.
#It is calling the insert_user_message_in_db function to insert the message in the database.
#It is redirecting the user to the / route.
#
#@app.route('/')
#def index():
#    db = get_db_connection()
#    cursor = db.cursor()
#

@app.route('/post', methods=['POST'])
def post():
    username = request.form['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect('/')