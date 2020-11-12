def wypisz(x):
    wiersz = [1]
    
    for _ in range(x):
        print(wiersz)
        wiersz = [1] + [wiersz[i] + wiersz[i+1] for i in range(len(wiersz) - 1)] + [1]
    
    
n = int(input('Podaj liczbe n: '))
wypisz(n)