import xml.etree.ElementTree as et

def coma_conv(word):
    for i in range(len(word)):
        if(word[i] == ','):
            word[i] = '.'
    return ''.join(word)

def appender(x):
    arr = []
    for i in x:
        arr.append(i.text)
    return arr


class Ex:
    def __init__(self, x):
        self.x = x
        self.file = et.parse(self.x)
        self.root = self.file.getroot()
    
    def l_ex(self):
        return appender(self.root.iter('nazwa_waluty'))
   
    def conv(self, val, i):
        arr = appender(self.root.iter('kurs_sredni'))
        arr2 = appender(self.root.iter('przelicznik'))
        kurs = coma_conv(list(arr[i]))
        przelicznik = arr2[i]
        return float(kurs) * val * int(przelicznik)
    
    def conv_ad(self, val, i, j):
        arr = appender(self.root.iter('kurs_sredni'))
        arr2 = appender(self.root.iter('przelicznik'))
        curr1 = coma_conv(list(arr[i]))
        curr2 = coma_conv(list(arr[j]))
        przelicznik1 = arr2[i]
        przelicznik2 = arr2[j]
        pln = val/float(curr1) * int(przelicznik1)
        return pln * float(curr2) * int(przelicznik2)
        
            

    
#path = 'kurs.xml'
path = input('Podaj sciezke pliku xml: ')
k = Ex(path)
while True:
    choice = input('Co chcesz abym zrobil? (wpisz 1 jesli chcesz zobaczyc liste kursow, 2 jesli chcesz przekonwertowac zlotowki na inna walute, 3 jesli chcesz przekonwertowac obca walute na inna walute: ')
    
    if(choice == '1'):
        Lofex = list(k.l_ex())
        for i in range(len(Lofex)):
            print(str(i + 1) + ' ' + Lofex[i])
    
    elif(choice == '2'):
        currency = int(input('Podaj numer waluty, na ktora chcesz przekonwertowac: ')) - 1
        value = float(input('Ile zlotych chcesz przekonwertowac?: '))
        print(str(value) + ' zlotych to ' + str(k.conv(value, currency)) + ' ' + str(k.l_ex()[currency]))
    
    elif(choice == '3'):
        currency1 = int(input('Podaj numer waluty, ktora chcesz przekonwertowac: ')) - 1
        value = float(input('Podaj ilosc waluty, ktora chcesz przekonwertowac: '))
        currency2 = int(input('Podaj numer waluty, na ktora chcesz przekonwertowac: ')) - 1
        print(str(value) + ' ' + str(k.l_ex()[currency1]) + ' to ' + str(k.conv_ad(value, currency1,currency2)) + ' ' + str(k.l_ex()[currency2]))
    
    else:
        print('Blednie wprowadzone polecenie :( ')
        continue
print(k.conv(14,0))
print(k.conv(14,1))
print(k.conv_ad(52.2242,1,0))
