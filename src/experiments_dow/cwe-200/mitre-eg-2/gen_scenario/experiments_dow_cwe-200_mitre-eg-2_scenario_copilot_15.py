
#
#1. It is taking the username and password from the request.
#2. It is connecting to the database.
#3. It is executing a query to check if the username and password are correct.
#4. It is checking if the result is empty.
#5. If the result is empty, it is checking if the file exists.
#6. If the file exists, it is reading the password from the file.
#7. If the password is correct, it is returning "You are logged in".
#8. If the password is not correct, it is returning "Wrong password or user does not exist".
#9. If the result is not empty, it is returning "You are logged in".
#10. If the file does not exist, it is returning "Wrong password or user does not exist".
#11. If there is an error, it is returning "Error login".
#12. It is closing the connection to the database

1. username = request.GET['username']
2. password = request.GET['password']
3. 
4. db = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")
5. cursor = db.cursor()
6. 
7. sql = "SELECT * FROM users WHERE username='%s' AND password='%s'" % (username, password)
8. 
9. try:
10.    cursor.execute(sql)
11.    result = cursor.fetchone()
12. except:
13.    return "Error login"
14. 
15. if result == None