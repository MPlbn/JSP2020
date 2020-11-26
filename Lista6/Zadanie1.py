import trojkat as t

while True:
    x = int(input('Podaj pierwszy bok: '))
    y = int(input('Podaj drugi bok: '))
    z = int(input('Podaj trzeci bok: '))
    
    if((x + y <= z) or (x + z <= y) or (y + z <= x)):
        print('Taki trojkat nie istnieje, podaj poprawne boki')
    else:
        break

o = t.obw(x,y,z)
p = t.pole(x,y,z)
typ_b = t.bok_typ(x,y,z)
k = t.kat(x,y,z)
typ_k = t.kat_typ(k)
    
print('Obwod trojkata to:' + str(o))
print('Pole trojkata to: ' + str(p))
print(typ_b)
print(typ_k)