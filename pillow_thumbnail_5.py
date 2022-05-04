from PIL import Image

im = Image.open('image.jpg')
thumbnail = im.resize((300, 300))
thumbnail.save('resized.jpg')
