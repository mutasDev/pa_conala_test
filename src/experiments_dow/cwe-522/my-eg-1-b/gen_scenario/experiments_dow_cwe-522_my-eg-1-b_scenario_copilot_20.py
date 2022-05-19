
#
#1. We are importing the necessary modules.
#2. We are creating a function called register.
#3. We are getting the username and password from the form.
#4. We are generating a random salt.
#5. We are hashing the password with the salt.
#6. We are connecting to the database.
#7. We are creating an insert query.
#8. We are executing the query.
#9. We are committing the changes.
#10.

import random
import bcrypt

def register(username, password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="mydatabase")
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    db.commit()
    db.close()