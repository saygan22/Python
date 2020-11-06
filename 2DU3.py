import string

velkaP = []
for x in [string.ascii_uppercase]:
   for y in list(x):
       velkaP.append(y)

print(velkaP)



sifrovane = input("Napiste sifrovane")
print("Это то, что вы только что ввели?", sifrovane)



shift = 0
while shift < 25:
  shift += 1
  def decryptCaesar(msg):
    zmena = ""
    for x in msg:
        if x in velkaP:

            ind = velkaP.index(x)
            zmena += velkaP[ind - shift]
        else:
            zmena += x
    return zmena
  print(decryptCaesar(sifrovane))

