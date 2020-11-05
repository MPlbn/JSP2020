def n_elem_ciag(numer_wyrazu, pierwszy_wyraz, roznica):
    x = list(range(1, numer_wyrazu))
    for i in x:
        pierwszy_wyraz *= roznica
    print('a' + str(numer_wyrazu) + ' = ' + str(pierwszy_wyraz))



n = int(input('Podaj n: '))

while True:
    pytanie = input('Czy chcesz wprowadzic swoje dane?(tak/nie): ')
    if (pytanie == 'tak'):
        a1 = int(input('Podaj pierwszy element ciagu: '))
        q = int(input('Podaj q: '))
        break
    elif (pytanie == 'nie'):
            a1 = 1
            q = 2
            break
    else:
        print('niepoprawnie wpisana odpowiedz!')

n_elem_ciag(n, a1, q)
