def silnia(n):
    x = list(range(1, int(n)+1))
    y = 1
    for i in x:
        y *= i
    print(y)
        
        
a = input('Wprowadz liczbe "n": ')
silnia(a)