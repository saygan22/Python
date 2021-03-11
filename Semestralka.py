import numpy
from PIL import Image

# im_gray = np.array(Image.open('volcano.pnm').convert('1'), dtype='uint8')
image = Image.open('volcano_PNG48.png')

image.save('volcano.pnm')
img = Image.open('volcano.pnm')

black_white = img.convert("1")
black_white.save('black_white.pnm')

img_black_white = Image.open('black_white.pnm')
img_black_white.show()
weight, height = img_black_white.size
print(weight)
print(height)



t = 0

pix = img_black_white.load()

last_index = weight - 1
print(type(bin(img_black_white.getpixel((last_index, 1)))))


g = 0
while(g < height):
    print(bin(img_black_white.getpixel((last_index, g))))
    g = g + 1

# f = open('black_white.pnm', 'rb+')
# for x in f.readlines():
#
#      t = t + 1
#      print(t)
#      print(x)






text = input("Enter message to encode: ").lower()
t2b = bin(int.from_bytes(text.encode(), 'big'))
print(t2b)


n = int(t2b, 2)
b2t = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
print(b2t)












