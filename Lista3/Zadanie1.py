a = input('Wpisz litere (bez polskich znaków): ')
samogloski = ['a', 'e', 'o', 'i', 'u', 'y']
spolgloski = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm' ]
if a in spolgloski:
    print('Litera '+ a +' to spolgloska')
elif a in samogloski:
    print('Litera '+ a +' to samogloska')
else:
    print('Litera jest wadliwa')