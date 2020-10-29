a = 0
b = 1
n = input('Podaj liczbe: ')
i = 0
while True:
    i += 1
    print(str(a) + ' ')
    if (i == int(n) ):
        break
    else:
        nast = a+b
        a = b
        b = nast
        continue