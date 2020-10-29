a = ['Kasia', 'Basia', 'Marek', 'Darek']
a.append('Józek')
b = ['Ania', 'Basia']
a.extend(b)
a.sort()
print(a[3])
print(a[0] + ' ' + a[1])
print(a[-2] + ' ' + a[-1])
x = a.count('Basia')
for i in range(x):
    a.remove('Basia')
ilosc_studentow = len(a)
a = tuple(a)