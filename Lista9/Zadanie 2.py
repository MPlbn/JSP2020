import numpy as n

choice = input('Chcesz wprowadzic dane recznie czy uzyc pliku?(recznie/plik)')
if(choice == 'recznie'):
    values = input('Wpisz liczby i oddziel je spacja: ')
elif(choice == 'plik'):
    path = input('Podaj sciezke pliku: ')
    try:
        file = open(path, 'r')
    except:
        print('Blad! nie ma takiego pliku!')
    else:
        values = file.read()
values = values.split(' ')
for i in range(len(values)):
    values[i] = int(values[i])
    
av = n.average(values)
var = n.var(values)
deviation = n.std(values)

print('Srednia: ' + str(av) + '\twariancja: ' + str(var) + '\todchylenie standardowe: ' + str(deviation))