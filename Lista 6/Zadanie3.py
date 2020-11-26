def mateusz(x):
    if(x == 1):
        return '1'
    elif(x == 2):
        return '11'
    else:
        a = list(mateusz(x-1))
        
        for i in range(0, len(a) - 1): # Od tej linijki cos nie dziala :(
            nowa = []
            zliczanie = 1
            if(a[i] == a[i+1]):
                zliczanie += 1
            else:
                powtorka = str(a[i])
                nowa.append(str(zliczanie) + powtorka)
    return ''.join(nowa)
                
        


n = int(input('Podaj liczbe n: '))

for i in range(1,n):
    x = mateusz(i)
    print(x)