
#
#1. The upload_image() function is called when the user uploads an image.
#2. The image is read and stored in a variable called img_data.
#3. The image is written to a file in the static/img directory.
#4. The image is read again and encoded as a base64 string.
#5. The base64 string is returned to the user.
#
#The base64 string is returned to the user because it is needed to

def upload_image(img_data):
    with open('static/img/image.png', 'wb') as f:
        f.write(img_data)
    with open('static/img/image.png', 'rb') as f:
        return base64.b64encode(f.read())