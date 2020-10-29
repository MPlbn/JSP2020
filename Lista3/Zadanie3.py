import math

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if(a == 0):
    print('To nie jest funkcja kwadratowa. Program zostanie za chwilę zamknięty')    
else:  
    delta = b**2 - 4*a*c
    if(delta < 0):
        print('Funcja nie ma rozwiązań. Program zostanie za chwilę zamknięty')
    elif(delta > 0):
        pdelta = math.sqrt(delta)
        x1 = (-b + pdelta) / 2*a
        x2 = (-b - pdelta) / 2*a
        print('x1 = ' + str(x1))
        print('x2 = ' + str(x2))
    else:
        pdelta = math.sqrt(delta)
        x0 = -b / 2*a
        print('x0 = ' + str(x0))
    