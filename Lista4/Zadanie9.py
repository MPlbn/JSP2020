def silnia(n):
    y = 1
    for i in range(1, n+1):
        y *= i
    print(y)
        
        
a = int(input('Wprowadz liczbe "n": '))
silnia(a)