
#
#1. The user enters a username and password into the form.
#2. The username and password are sent to the server.
#3. The server hashes the password and inserts the username and hashed password into the database.
#4. The server redirects the user to the home page.
#
#The code above is vulnerable to SQL injection. The username and password are not sanitized before being inserted into the database.
#
#The following code is vulnerable to SQL injection:

import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

conn.commit()

conn.close()