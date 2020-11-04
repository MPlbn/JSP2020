m = int(input('podaj pierwsza liczbe calkowita: '))
n = int(input('podaj druga liczbe calkowita: '))

i = list(range(1, m + 1))
j = list(range(1, n + 1))
for x in i:
    print('')
    for y in j:
        print(x*y, end = '\t\t\t')