
#
#1. The user enters the stock name and quantity in the form.
#2. The form is submitted to the buy_order route.
#3. The buy_order route takes the stock name and quantity and inserts it into the database.
#
#Now, we need to create a route that will display the user's tradepile.
#
#@app.route('/tradepile')
#def tradepile():
#    username = session['username']
#

@app.route('/tradepile')
def tradepile():
    username = session['username']
    tradepile = db.execute("SELECT * FROM tradepile WHERE username = :username",
                          {"username": username}).fetchall()
    return render_template("tradepile.html", tradepile=tradepile)