from PIL import Image
im = Image.open('road.jpg')
print(im.format, im.size, im.mode)
im.show()