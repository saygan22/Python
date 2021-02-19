pocet_radku = int(input('Pocet radek'))
k = 0
while k < pocet_radku:
    xs = ''
    for u in range(k + 1):
      xs = xs + '&'
      if u != k:
          xs = xs + ' '

    print(xs.center(pocet_radku*2))
    k = k + 1