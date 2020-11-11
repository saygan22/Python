
def prvniZluta(k,j):
  for k in range(27):
    for j in range(1):
        if (k + j) % 2 == 0:
            print('\033[' + str(43) + 'm', end="\t")
        else:
            print('\033[' + str(44) + 'm', end="\t")
  print()

def prvniModra(x,t):
  for x in range(27):
    for t in range(1,2):
        if (x + t) % 2 == 0:
            print('\033[' + str(43) + 'm', end="\t")
        else:
            print('\033[' + str(44) + 'm', end="\t")
  print()



for i in range(1,20):
    if i%2 != 0:
        prvniZluta(27, 1)
    if i%2 == 0:
        prvniModra(27, range(1,2))



