def dzielnik(x,y):
    while True:
        if (x == y):
            break
        else:
            if (x>y):
                x -= y
            elif (y>x):
                y -= x
    print('Najwiekszy wspolny dzielnik to: ' + str(x))
    
a = int(input('Podaj pierwsza liczbe calkowita: '))
b = int(input('Podaj druga liczbe calkowita: '))
dzielnik(a,b)