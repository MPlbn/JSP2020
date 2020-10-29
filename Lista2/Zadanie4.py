a = input('Wpisz słowo: ')
a = list(a)
i = 0
x = len(a)
while i<x:
    if(a[i] == a[0]):
        a[i] = '$'
    else:
        continue
    i +=1
print(a)
        

        