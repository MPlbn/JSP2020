def szyfruj(x):
    pusta = []
    for i in x:
        if(i == 'a'):
            a = 'y'
        elif(i == 'e'):
            a = 'i'
        elif(i == 'i'):
            a = 'o'
        elif(i == 'o'):
            a = 'a'
        elif(i == 'y'):
            a = 'e'
        else:
            a = i
        pusta.append(a)
    x = pusta
    return x

def deszyfruj(x):
    pusta = []
    for i in x:
        if(i == 'y'):
            a = 'a'
        elif(i == 'i'):
            a = 'e'
        elif(i == 'o'):
            a = 'i'
        elif(i == 'a'):
            a = 'o'
        elif(i == 'e'):
            a = 'y'
        else:
            a = i
        pusta.append(a)
    x = pusta
    return x
    
def dowys(x):
    y = ''.join(x)
    return y
        
a = list(input('Podaj slowo: '))
b = szyfruj(a)
c = deszyfruj(b)
zaszyf = str(dowys(b))
deszyf = str(dowys(c))
print(zaszyf)
print(deszyf)
