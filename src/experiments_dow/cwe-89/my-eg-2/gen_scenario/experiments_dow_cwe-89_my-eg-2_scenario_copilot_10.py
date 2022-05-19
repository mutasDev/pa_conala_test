
#
#1. It is getting the username and message from the request.
#2. It is calling the insert_user_message_in_db function to insert the message in the database.
#3. It is redirecting the user to the home page.
#
#Now, let's add the code to display the messages.
#
#Open the index.html file and add the following code:
#
#<div class="container">
#    <div class="row">
#

def insert_user_message_in_db(username, message):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Insert the message in the database
    c.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))

    # Save the changes
    conn.commit()

    # Close the connection
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the data from the form
        username = request