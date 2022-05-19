
#
#1. The user enters a username and password.
#2. The username and password are sent to the server.
#3. The server checks the database to see if the username and password are correct.
#4. If the username and password are correct, the server sends the user to the home page.
#5. If the username and password are incorrect, the server sends the user back to the login page.
#
#The code above is not complete. You need to add

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    data = {"username": username, "password": password}

    response = requests.post("http://localhost:5000/login", json=data)

    if response.status_code == 200:
        print("Login successful!")
    else:
        print("Login failed.")