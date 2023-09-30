a = "01101000 01101001 00100000 01110010 01110101 01110010 01101100"
a = a.split()
l = [list("woofwoof") for i in range(len(a))]
for i, binary in enumerate(a):
    for j, letter in enumerate(binary):
        if letter == '1':
            l[i][j] = l[i][j].upper()
for binary in l:
    print(''.join(binary))
