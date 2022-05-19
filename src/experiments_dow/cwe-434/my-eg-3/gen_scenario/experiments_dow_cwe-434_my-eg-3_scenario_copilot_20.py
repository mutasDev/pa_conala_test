
#
#1. We are creating a Flask app.
#2. We are creating a function that will check if the file is safe.
#3. We are creating a route that will handle the file upload.
#4. We are getting the file from the request.
#5. We are getting the name and extension of the file.
#6. We are checking if the file is safe.
#7. We are saving the file to the uploads folder.
#8. We

1. import os
2. from flask import Flask, request, redirect, url_for
3. from werkzeug.utils import secure_filename
4. 
5. app = Flask(__name__)
6. app.config['UPLOAD_FOLDER'] = 'uploads'
7. 
8. def is_safe_file(filename):
9.     return '.' in filename and \
10.            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
11. 
12. @app.route('/', methods=['GET', 'POST'])
13. def upload_