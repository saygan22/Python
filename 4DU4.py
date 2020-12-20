with open('Duha.ppm', 'bw') as f:
    f.write(b'P6 256 256 255 ')
    radek = bytearray()
    for i in range(256):
            pixel1 = bytearray( [255, i, 0] )
            radek.extend(pixel1)

    j = 255
    l = 255
    while j > 128:
        l = l - 2
        j = j - 1
        pixel2 = bytearray([l, j, 0])
        radek.extend(pixel2)

        if (j == 128) or (l == 0):
            k = 0
            while j > 1:
                k = k + 2
                j = j - 1
                pixel2 = bytearray([l, j, k])
                radek.extend(pixel2)

    r = 0
    u = 255
    while r < 70:
        r = r + 1
        u = u - 2
        pixel3 = bytearray([r, 0, u])
        radek.extend(pixel3)


    e = 70
    y = 0
    h = 140
    while e < 238:
        e = e + 5
        y = y + 4
        h = h + 3
        pixel4 = bytearray([e, y, h])
        radek.extend(pixel4)

    f.write(radek)








