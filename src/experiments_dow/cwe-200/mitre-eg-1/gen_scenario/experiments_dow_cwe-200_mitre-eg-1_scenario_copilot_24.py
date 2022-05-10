
#
#1. It is connecting to the database.
#2. It is checking if the username and password are in the database.
#3. If they are, it returns true.
#4. If they are not, it returns false.
#
#Now, we need to create a file called login.html. This is the file that will be displayed to the user.
#
#<html>
#<head>
#<title>Login</title>
#<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
#<script>
#$(document).ready(function(){
#    $("

def login(username, password):
    """
    This function will check the database to see if the
    username and password are in there.
    """
    # Connect to the database
    db = connect()
    
    # Check if the username and password are in the database
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    
    # If they are, return true
    if result:
        return True
    
    # If they are not, return false
    else:
        return False