import numpy as np
from PIL import Image
np.set_printoptions(threshold=100000000, linewidth=999999) # pro moznost prohlizet cele pole ndrarray

dict = {'A': '11001', 'B': '00001', 'C': '00010', 'D': '00100', # slovnik pro system 5 bitoveho kodovani/dekodovani
        'E': '01000', 'F': '10000', 'G': '00011', 'H': '00110',
        'I': '01100', 'J': '11000', 'K': '00111', 'L': '01110',
        'M': '11100', 'N': '01111', 'O': '11110', 'P': '11111',
        'Q': '00101', 'R': '01010', 'S': '10100', 'T': '01001',
        'U': '10010', 'V': '10001', 'W': '10101', 'X': '11011',
        'Y': '11101', 'Z': '10111',
        '.': '11010', ',': '01011',  ' ': '10011'}



def image_to_array(name_of_image): # změní obrázek na černobílý a vrátí pole
    im = Image.open(name_of_image)
    im = im.convert('1')
    pixels = np.array(im, dtype='int8')
    return pixels

choose_a_function = input("Choose function: encode or decode.\n"
                          "Encode - write 1\n"
                          "Decode - write 2\n")
if choose_a_function == str(1):
    text = input("Enter message to encode: ").upper()
    def encode(text):
        list_encoded = ''
        for letter in text:
            for key in dict:
                if key == letter:
                    list_encoded = list_encoded + (dict[key])
        return list_encoded

    name_of_image_to_encode = input("Enter name of image to encode vcetne formatu: \n")
    pixels_to_encode = image_to_array(name_of_image_to_encode)
    height, weight = pixels_to_encode.shape
    print('Weight divided by eight per module (%) =', weight%8, 'Remember the number !!! ', ' If zero, '
           "\n In 'Enter the number of extra columns' in which the message is encrypted WRITE 8 !!!\n")

    const_encoded = weight % 8 # doplnek osmi
    if const_encoded == 0:
        const_encoded = 8

    list_of_encoded = []
    for f in encode(text):
        list_of_encoded.append(int(f))  # vytvoři seznam čísel jako kód, jednu číslici po druhé
    b = np.array(list_of_encoded, dtype=np.int8)  # vytvoři vektorové pole z číselného kódu
    b.resize((height, const_encoded), refcheck=False)  # vytvoři chybějící proužek obrázku, přebytek vyplni nulami
    encoded_im = np.column_stack([pixels_to_encode, b])  # spojujeme hlavní a kódované části

    name_of_encoded_file = input('Enter name of encoded image,without formatu\n')
    img = Image.fromarray((encoded_im * 255).astype('uint8'), mode='L').save(
        name_of_encoded_file + '.pnm')  # přeložit zpět do obrázku
    pic = Image.open('pic2.pnm')
    pic.show()  # Varianta PNM P5, kódovaný proužek je vidět vpravo

elif choose_a_function == str(2):
    name_of_image_to_decode = input("Enter name of image to decode: \n")
    pixels_to_decode = (image_to_array(name_of_image_to_decode))
    height, weight = pixels_to_decode.shape
    const_decoded = weight % 8
    count_of_nadbytečných_sloupců = int(input("Enter the number of extra columns in which the message is encrypted: \n"))
    number_of_last_normal_column = weight - count_of_nadbytečných_sloupců

    encoded_column_for_decode = pixels_to_decode[0:, number_of_last_normal_column:weight]
    o = 0
    str1 = ''
    decoded_message = ''
    for x in np.nditer(encoded_column_for_decode):
        o = o + 1
        str1 = str1 + str(x)
        if (o % 5) == 0:
                for key, value in dict.items():
                    if value == str1:
                        decoded_message = decoded_message + key
                        o = 0
                        str1 = ''
                        break
    print('Decoded message is\n', decoded_message)

    # t = 0
    # f = open('pic2.pnm', 'rb+')
    # for x in f.readlines():  # přímé čtení souboru
    #     t = t + 1
    #     print('Number of line', t)
    #     print(x)
else: print('Error,please try again')


# img2 = Image.fromarray(encoded_im, mode='L')
# img2.save('pic6.pnm')
# img3 = Image.open('pic6.pnm').convert("1")
# img3.save('pic7.pnm')
# img3.show() # вариант PNM P4 но выводит черное изображение

# t = 0
# f = open('pic7.pnm', 'rb+')
# for x in f.readlines(): # прямое чтение файла
#      t = t + 1
#      print('Number of line',t)
#      print(x)



