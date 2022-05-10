
#
#1. The user enters a username and password into the form.
#2. The form sends a POST request to the server.
#3. The server receives the POST request and checks the database for a username that matches the form username.
#4. If there is a match, the server checks the database for a hashed password that matches the form password.
#5. If there is a match, the server returns "success" to the client.
#6. If there is no match, the server returns "wrong pw" to the client.
#7. If there is no username match, the server returns "username not found" to the client.
#
#I am trying to figure out how to do the following:
#
#1. If the server returns "success" to the client, the client should redirect to a new page.
#2. If the server returns "wrong pw" to the client, the client should display an error message.

1. If the server returns "success" to the client, the client should redirect to a new page.

if (success):
    redirect("newpage.html")

2. If the server returns "wrong pw" to the client, the client should display an error message.

if (wrong_pw):
    print("Error: wrong password")