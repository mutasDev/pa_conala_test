
#
#1. We are creating a Flask app.
#2. We are creating a route called /check_mod.
#3. We are getting the username and password from the request.
#4. We are checking if the username and password are correct.
#5. We are returning true or false based on the result.
#
#Now, we need to create a file called app.yaml. This file will tell Google App Engine how to run our application.
#
#Create

app.yaml

runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /check_mod
  script: main.app

libraries:
- name: flask
  version: 0.10.1

Now, we need to deploy our application to Google App Engine.

To do this, we need to run the following command:

appcfg.py -A <your-app-id> -e <your-email> update .

Replace <your-app-id> with the ID of your application and <your-email> with your email address.

You should see a message that