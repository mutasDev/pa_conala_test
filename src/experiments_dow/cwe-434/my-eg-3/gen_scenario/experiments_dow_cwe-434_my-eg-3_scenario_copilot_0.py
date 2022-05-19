
#
#1. The upload_file() function is called when a POST request is made to the /file/upload endpoint.
#2. The request.files['f'] is the file that was uploaded.
#3. The file_is_safe_type() function is called to check if the file is a safe type.
#4. The file is saved to the uploads directory.
#5. The user is redirected to the /file/upload endpoint.
#
#The

def upload_file():
    if request.method == 'POST':
        if 'f' in request.files:
            f = request.files['f']
            if file_is_safe_type(f.filename):
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
                return redirect(url_for('upload_file'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-