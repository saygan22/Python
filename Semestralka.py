import numpy
from PIL import Image

image = Image.open('volcano_PNG48.png')

image.save('volcano.pnm')
img = Image.open('volcano.pnm')

black_white = img.convert("1")
black_white.save('black_white.pnm')

img_black_white = Image.open('black_white.pnm')
img_black_white.show()
weight, height = img_black_white.size
print(weight)
f = open('black_white.pnm', 'rb+')
str = ''
t = 0

pix = img_black_white.load()
xb = bytearray()
last_index = weight - 1

g = 0
while(g < height):
    print(bin(img_black_white.getpixel((last_index, g))))

    g = g + 1



for x in f.readlines():

     t = t + 1
     print(t)
     print(x)



img_array = numpy.asarray(f, dtype='uint8')
print(img_array)