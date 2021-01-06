def test_kontrol(x):
    algorytm = 1*int(x[0]) + 3*int(x[1]) + 7*int(x[2]) + 9*int(x[3]) + 1*int(x[4]) + 3*int(x[5]) + 7*int(x[6]) + 9*int(x[7]) + 1*int(x[8]) + 3*int(x[9]) + 1*int(x[10])
    if(algorytm%10 == 0):
        return 1
    else:
        return 0
    
def test_plec(x):
    if(x%2 == 0):
        return 'kobieta'
    else:
        return 'mezczyzna'
    
def msc_test(x):
    if(x[0] in '80246'):
        return x[1]
    elif(x[0] in '91357'):
        return '1' + x[1]
        
def rok_test(x):
    final = x[0] + x[1]
    if(x[2] in '89'):
        final = '18' + final
    elif(x[2] in '0246'):
        pre = 19 + int(x[2])//2
        final = str(pre) + final
    else:
        pre = 19 + (int(x[2])-1)//2
        final = str(pre) + final
    return final

def data_ur(x):
    dzien = x[4] + x[5]
    msc = msc_test(x[2:4])
    rok = rok_test(x[0:3])
    return 'data urodzenia ' + dzien + '-' + msc + '-' + rok
    
try:
    file = open("PESEL.txt", "r")
except:
    print('Plik nie istnieje')
else:
    save = open("PESEL_opis.txt", "w")
    inside = file.read()
    pesele = inside.split(' ')
    
    for i in pesele:
        valid = test_kontrol(i)
        if(valid == 1):
            plec = test_plec(int(i[9]))
            ur = data_ur(i[0:6])
            save.write('nr '+i+':\n'+ ur +';\tpłeć: ' + plec + '\n\n')
    save.close()
    file.close()