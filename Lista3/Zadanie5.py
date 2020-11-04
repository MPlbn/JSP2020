import string

haslo = list(input('Wprowadz haslo: '))
male_l = list(string.ascii_lowercase)
duze_l = list(string.ascii_uppercase)
numery = list(range(0,9))
z_spec = ['$', '#', '@']
blad = 'Bledne haslo! Zamykam program!!!'
i = 4


if (len(haslo) <= 16 and len(haslo) >= 6):
    i -= 1
    
else:
    i = i    

for x in male_l:
    if (x in haslo):
        i -= 1
        break
    else:
        continue

for x in duze_l:
    if (x in haslo):
        i -= 1
        break
    else:
        continue

for x in numery:
    if (x in haslo):
        i -= 1
        break
    else:
        continue

for x in z_spec:
    if (x in haslo):
        i -= 1
        break
    else:
        continue

if(i == 0):
    print('Twoje haslo jest poprawne')
else:
    print('Twoje haslo jest niepoprawne! Ilosc bledow: ' + str(i))