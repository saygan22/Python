import numpy as np
from PIL import Image

print(np.sctypeDict) # разновидности елементов массива
im = Image.open('zhivotnie_grach.gif') # создаем елемент pillow для превращения
im  = im.convert('1') # делаем черно-белым
im.show()
print(type(im))
pixels = np.array(im, dtype='int8')
weight, height = im.size

np.set_printoptions(threshold=100000000, linewidth=2666)

print(pixels.reshape(weight, height)) #  вывод массива
print(weight)
print(height)
print(type(pixels)) # тип массива
print(type(pixels[10, 10])) # тип ячейки массива(пикселя)
print(pixels.size) # количевство пикселей(елементов массива)
a = weight%8
print(weight%8) # остаток от деления на 8
print(pixels.itemsize) # размер ячейки в битах
print(pixels.size*pixels.itemsize) # размер в битах

dict = {'A': '00000', 'B': '00001', 'C': '00010', 'D': '00100',
        'E': '01000', 'F': '10000', 'G': '00011', 'H': '00110',
        'I': '01100', 'J': '11000', 'K': '00111', 'L': '01110',
        'M': '11100', 'N': '01111', 'O': '11110', 'P': '11111',
        'Q': '00101', 'R': '01010', 'S': '10100', 'T': '01001',
        'U': '10010', 'V': '10001', 'W': '10101', 'X': '11011',
        'Y': '11101', 'Z': '10111',
        '.': '11010', ',': '01011', '?': '11001', ' ': '10011'}
text = input("Enter message to encode: ").upper()

def encode(text):
    list_encoded = ''
    for letter in text:
        for key in dict:
            if key == letter:
                list_encoded = list_encoded + (dict[key])
    return list_encoded
print(encode(text))

last_pixels = np.zeros((height, a), dtype=np.int8) #создаем пустой массив нулей заданой формы



list_of_encoded = []
for f in encode(text):
   list_of_encoded.append(int(f)) # создаем список чисел в виде кода по одной цифре


b = np.array(list_of_encoded, dtype=np.int8) # создаем векторный масив из кода цифр
print(b)


b.resize((height, a), refcheck=False) # создаем недостающую полосу изображения, лишнее заполняем нулями
print(b)
print(pixels)
encoded_im = np.column_stack([pixels, b]) # соединяем основную и закодированную части


print(encoded_im)
print(encoded_im.shape)


# img = Image.fromarray((encoded_im * 255).astype('uint8'), mode='L').save('pic2.pnm') #  переводим назад в изображение
# pic = Image.open('pic2.pnm')
# pic.show() # вариант PNM P5, справа видна закодированная полоса


img2 = Image.fromarray(encoded_im, mode='L')
img2.save('pic6.pnm')

img3 = Image.open('pic6.pnm')
img4 = img3.convert("1")
img4.save('pic7.pnm')
img4.show() # вариант PNM P4 но выводит черное изображение


t = 0
f = open('pic7.pnm', 'rb+')
for x in f.readlines(): # прямое чтение файла
     t = t + 1
     print(t)
     print(x)