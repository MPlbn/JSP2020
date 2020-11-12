def jednosci(x):
    if (x == 1):
        y = 'jeden'
    elif (x == 2):
        y = 'dwa'
    elif (x == 3):
        y = 'trzy'
    elif (x == 4):
        y = 'cztery'
    elif (x == 5):
        y = 'piec'
    elif (x == 6):
        y = 'szesc'
    elif (x == 7):
        y = 'siedem'
    elif (x == 8):
        y = 'osiem'
    elif (x == 9):
        y = 'dziewiec'
    elif (x == 0):
        y = ''
    return y

def dzies_dla_jed(x):
    if (x == 0):
        y = 'dziesiec'
    elif (x == 1):
        y = 'jedenascie'
    elif (x == 2):
        y = 'dwanascie'
    elif (x == 3):
        y = 'trzynascie'
    elif (x == 4):
        y = 'czternascie'
    elif (x == 5):
        y = 'pietnascie'
    elif (x == 6):
        y = 'szesnascie'
    elif (x == 7):
        y = 'siedemnascie'
    elif (x == 8):
        y = 'osiemnascie'
    elif (x == 9):
        y = 'dziewietnascie'  
    return y

def dziesiatki(x):
    if (x == 0):
        y = ''
    elif (x == 2):
        y = 'dwadziescia'
    elif (x == 3):
        y = 'trzydziesci'
    elif (x == 4):
        y = 'czterdziesci'
    elif (x == 5):
        y = 'piecdziesiat'
    elif (x == 6):
        y = 'szescdziesiat'
    elif (x == 7):
        y = 'siediemdziesiat'
    elif (x == 8):
        y = 'osiemdziesiat'
    elif (x == 9):
        y = 'dziewiecdziesat'
    return y

def setki(x):
    if (x == 1):
        y = 'sto'
    elif (x == 2):
        y = 'dwiescie'
    elif (x == 3):
        y = 'trzysta'
    elif (x == 4):
        y = 'czterysta'
    elif (x == 5):
        y = 'piecset'
    elif (x == 6):
        y = 'szescset'
    elif (x == 7):
        y = 'siedemset'
    elif (x == 8):
        y = 'osiemset'
    elif (x == 9):
        y = 'dziewiecset'
    elif (x == 0):
        y = ''
    return y
    
def tysiace(x):
    if (x == 1):
        y = 'tysiac'
    elif (x == 0):
        y = ''
    else:
        y = '!ZLA WARTOSC CYFYRY[tysiac]'
    return y

def zamien(x):
    if (len(x) == 1):
        y = jednosci(int(x[0]))
    elif (len(x) == 2):
        if (x[0] != 1):
            y = dziesiatki(int(x[0])) + ' ' + jednosci(int(x[1]))
        else:
            y = dzies_dla_jed(int(x[1]))
    elif (len(x) == 3):
        if (x[1] != 1):
            y = setki(int(x[0])) + ' ' + dziesiatki(int(x[1])) + ' ' + jednosci(int(x[2]))
        else:
            y = setki(int(x[0])) + ' ' + dzies_dla_jed(int(x[2]))
    elif (len(x) == 4):
        if (x[2] != 1):
            y = tysiace(int(x[0])) + ' ' + setki(int(x[1])) + ' ' + dziesiatki(int(x[2])) + ' ' + jednosci(int(x[3]))
        else:
            y = tysiace(int(x[0])) + ' ' + setki(int(x[1])) + ' ' + dzies_dla_jed(int(x[3]))
    
    return y

a = input('Wpisz liczbe: ')
a = list(a)
print(zamien(a))

