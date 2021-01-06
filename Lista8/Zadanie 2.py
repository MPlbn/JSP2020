import Szyfr as s
import datetime as dt
import os

def count_step(x):
    x = list(x)
    x.reverse()
    for i in range((len(x) - 1)):
        if(x[i] == '_'):
            if(x[i+1] == '0'):
                y = x[i+2] + x[i+1]
                break
            else:
                y = x[i+1]
                break
        else:
            continue
    return int(y)

path = input('Podaj sciezke zaszyfrowanego pliku (lub sama nazwe jesli znajduje sie w tym samym folderze co plik): ')
step = count_step(path)
try:
    file = open(path, 'r')
except:
    print('Plik nie istnieje')
else:
    inside = file.read()
    new = s.deszyfr(inside, step)
    cat_path = input('Podaj sciezke do zapisu nowego pliku bez nazwy pliku(zakonczona "/") (jesli ma byc w bierzacym katalogu, nie wpisuj nic): ')
    date = dt.datetime.now()
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    minute = str(date.minute)
    second = str(date.second)
    newfilename = cat_path + 'plik_deszyfrowany' + str(step) + '_' + year + month + day + minute + second + '.txt'
   
    i = 0
    while i<2:
        try:
            newfile = open(newfilename, "x")
        except:
            while True:
                try:
                    os.makedirs(cat_path)
                except:
                    break
            i += 1
        else:
            newfile.write(new)
            newfile.close()
            file.close()