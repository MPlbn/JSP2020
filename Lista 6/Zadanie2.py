import SzyfrCezara as sc

a = list(input('Podaj zdanie: '))
changed = sc.szyfr(a)
print('Twoje zdanie zaszyfrowane: ' + changed + ' || Twoje zdanie odszyfrowane: ' + sc.deszyfr(changed))