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
print('Encrypted file' + Encrypted_file)

p = 0
while p < len(key):
    p = p + 1
    one_of_variant = key[p]
    one_of_variant *= len(Encrypted_file)//len(one_of_variant) + 1
    v = ""
    for i, j in enumerate(Encrypted_file):
        gg = (ord(j) - ord(one_of_variant[i]))
        v += chr(gg % 26 + ord('A'))
    decrypt_list = (v)
    print("Number of one_of_variant sifry" + '\t' + str(p))
    print("Key" + '\t' + one_of_variant)
    print('Decrypted message:' + '\t' + decrypt_list + "\n")