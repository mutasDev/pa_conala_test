#resized image `image` to width, height of `(x, y)` with filter of `ANTIALIAS`


from PIL import Image

image = Image.open("image.jpg")

x = 100
y = 100

image = image.resize((x, y), Image.ANTIALIAS)

image.save("resized_image.jpg")