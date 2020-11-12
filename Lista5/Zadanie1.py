def zamiana(x):
    z = 0
   
    
    if (len(x) == 1):
        if (x[0] == 'jeden'):
            y = 1
        elif (x[0] == 'dwa'):
            y = 2
        elif (x[0] == 'trzy'):
            y = 3
        elif (x[0] == 'cztery'):
            y = 4
        elif (x[0] == 'piec'):
            y = 5
        elif (x[0] == 'szesc'):
            y = 6
        elif (x[0] == 'siedem'):
            y = 7
        elif (x[0] == 'osiem'):
            y = 8
        elif (x[0] == 'dziewiec'):
            y = 9
        elif x[0] == 'dziesiec':
            y = 10
        elif x[0] == 'jedenascie':
            y = 11
        elif x[0] == 'dwanascie':
            y = 12
        elif x[0] == 'trzynascie':
            y = 13
        elif x[0] == 'czternascie':
            y = 14
        elif x[0] == 'pietnascie':
            y = 15
        elif x[0] == 'szesnascie':
            y = 16
        elif x[0] == 'siedemnascie':
            y = 17
        elif x[0] == 'osiemnascie':
            y = 18
        elif x[0] == 'dziewietnascie':
            y = 19
        else:
            y = 'blad'
        
        
    elif (len(x) == 2):
        if (x[1] == 'jeden'):
            y = 1
        elif (x[1] == 'dwa'):
            y = 2
        elif (x[1] == 'trzy'):
            y = 3
        elif (x[1] == 'cztery'):
            y = 4
        elif (x[1] == 'piec'):
            y = 5
        elif (x[1] == 'szesc'):
            y = 6
        elif (x[1] == 'siedem'):
            y = 7
        elif (x[1] == 'osiem'):
            y = 8
        elif (x[1] == 'dziewiec'):
            y = 9
        else:
            y = 'blad'
            
        
        if x[0] == 'dwadziescia':
            z = 2
        elif x[0] == 'trzydziesci':
            z = 3
        elif x[0] == 'czterdziesci':
            z = 4
        elif x[0] == 'piecdziesiat':
            z = 5
        else:
            z = 'blad'

    if (y == 'blad' or z == 'blad'):
        print('Zle podana liczba')
    else:
        print(str(z) + str(y))


a = input('Wpisz liczbe slownie (1 - 59): ')
a = a.split(' ')
zamiana(a)
