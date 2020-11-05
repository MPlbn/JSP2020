def suma_har(n):
    x = list(range(1, int(n)+1))
    y = 0
    for i in x:
        y += 1/i
    print(y)
        
        
a = input('Wprowadz liczbe "n": ')
suma_har(a)