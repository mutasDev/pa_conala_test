
#
#1. The upload_file() function is called when a POST request is made to the /file/upload endpoint.
#2. The file is saved to the uploads directory.
#3. The file is checked to see if it is a safe file type.
#4. If the file is safe, the user is redirected to the /download endpoint.
#5. If the file is not safe, the file is deleted and the user is told that the file is not

def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join