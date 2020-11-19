def dodawanie(x):
    y = 0
    for i in x:
        if(i == 'I'):
            y += 1
        elif(i == 'V'):
            y += 5
        elif(i == 'X'):
            y += 10
        elif(i == 'L'):
            y += 50
        elif(i == 'C'):
            y += 100
        elif(i == 'D'):
            y += 500
        elif(i == 'M'):
            y += 1000
    return y

def odejmowanie(x,y):
    for i in range(len(x) - 1):
        if(x[i] == 'I' and (x[i+1] == 'M' or x[i+1] == 'D' or x[i+1] == 'C' or x[i+1] == 'L' or x[i+1] == 'X' or x[i+1] == 'V')):
            y -= 1 * 2
        elif(x[i] == 'V' and (x[i+1] == 'M' or x[i+1] == 'D' or x[i+1] == 'C' or x[i+1] == 'L' or x[i+1] == 'X')):
            y -= 5 * 2
        elif(x[i] == 'X' and (x[i+1] == 'M' or x[i+1] == 'D' or x[i+1] == 'C' or x[i+1] == 'L')):
            y -= 10 * 2
        elif(x[i] == 'L' and (x[i+1] == 'M' or x[i+1] == 'D' or x[i+1] == 'C')):
            y -= 50 * 2
        elif(x[i] == 'C' and (x[i+1] == 'M' or x[i+1] == 'D')):
            y -= 100 * 2
        elif(x[i] == 'D' and (x[i+1] == 'M')):
            y -= 500 * 2
    return y
            

def zamien(x):
   y = dodawanie(x)
   y = odejmowanie(x,y)
   return y
    
a = list(input('Podaj liczbe rzymska: '))
wynik = zamien(a)
print(wynik)
