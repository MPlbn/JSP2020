import Szyfr as s
import datetime as dt
import os

path = input('Podaj sciezke do pliku(lub sama nazwe jesli znajduje sie w tym samym folderze co plik): ')
step = int(input('O ile chcesz przesunac litery? 1-10: '))
try:
    file = open(path,'r')
except:
    print('Plik nie istnieje')
else:
    inside = file.read()
    new = s.szyfr(inside,step)
    cat_path = input('Podaj sciezke do zapisu nowego pliku bez nazwy pliku(zakonczona "/") (jesli ma byc w bierzacym katalogu, nie wpisuj nic): ')
    date = dt.datetime.now()
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    minute = str(date.minute)
    second = str(date.second)
    #Zmienilem sposob nazywania plikow, zeby dalo sie je rozroznic (dodalem minute i sekunde, w ktorej zostal utworzony)
    newfilename = cat_path + 'plik_zaszyfrowany' + str(step) + '_' + year + month + day + minute + second + '.txt'
   
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