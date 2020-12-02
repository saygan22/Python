print("Read the Crypt-file with Key-file")
print("Please create the Crypt-file without empty lines and Key-file")
with open("crypt.txt", "r") as file_crypt: something = file_crypt.read()
with open("key.txt", "r") as file_key: key = file_key.read().splitlines()


delims = ('.', '?', '!', ':', ';', '-', '(', ')', '[', ']', '"', ',')
something = something.upper()
for i in range(len(something)):
    for x in delims:
        if something[i] == x:
            something = something.replace(x, ' ')
print(something)

list = something.split()
Encrypted_file = ""
for x in list:
    Encrypted_file += x

list_key = (key)
test = ' '.join(list_key).upper()
list_key_upper = test.split()
# print(list_key_upper)
print('Encrypted file' + '\n' + Encrypted_file)

print(len(something))
print(len(Encrypted_file))

character_map = {
 ord('\n') : '',
 ord('\t') : '',
 ord('\r') : '',
 ord(',')  : '',
ord('.')  : '',
ord('!')  : '',
ord('"')  : '',
ord('?')  : '',
ord(';')  : '',
ord(':')  : ''
}
sifrovany_text = something.translate(character_map)
print(something.translate(character_map))
text = sifrovany_text.replace(' ', '*')
print(len(text))
print(text)
l = 0
set_mezer = []
for a in text:
    l = l + 1
    if a == '*':

      set_mezer.append(l)

print(set_mezer)

t = 0
p = 0
while p < len(key):

    one_of_variant = list_key_upper[p]
    p = p + 1
    one_of_variant *= len(Encrypted_file)//len(one_of_variant) + 1
    v = ""
    for i, j in enumerate(Encrypted_file):
        gg = (ord(j) - ord(one_of_variant[i]))
        v += chr(gg % 26 + ord('A'))


    # decrypt_list = v.split(' ')

    for value in list_key_upper:
        e = v.find(value)
        if e != -1:
            if len(value) > 6:
                print(value)
                print("Number of one_of_variant sifry" + '\t' + str(p))
                print("Key" + '\t' + one_of_variant)
                print('Decrypted message:' + '\t', v, "\n")
            # if value in v:
            #     t = t + 1

            #     print(t)
            # count_coincidence = {str(p) : t}


    # print(count_coincidence)

    # if t > 100000:
    #     #print(count_coincidence)
    #     print("Number of one_of_variant sifry" + '\t' + str(p))
    #     print("Key" + '\t' + one_of_variant)
    #     print('Decrypted message:' + '\t' , v , "\n")
    #     break


