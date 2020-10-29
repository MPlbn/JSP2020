
a = input('Wpisz słowo: ')
a = list(a)
i = 1
x = len(a)
while i<x:
    if((i != 0) and (a[i] == a[0])):
        a[i] = '$'
    i +=1
print(''.join(a))