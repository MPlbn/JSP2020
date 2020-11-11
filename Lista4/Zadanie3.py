import math
def stop_rad(x,y):
    if (x == 0 and y == 0):
        print('Nie zartuj, ze nic nie wpisales...')
    elif x == 0:
        rad = (y * math.pi) / 180
        print(str(y) + ' stopni przekonwertowane na radiany to: ' + str(rad))
    elif y == 0:
        deg = (x * 180) / math.pi
        print(str(x) + ' radianow przekonwertowanych na stopnie to: ' + str(deg))
    else:
        rad = (y * math.pi) / 180
        deg = (x * 180) / math.pi
        print(str(y) + ' stopni przekonwertowane na radiany to: ' + str(rad) + ', a ' + str(x) + ' 0radianow przekonwertowanych na stopnie to: ' + str(deg))
    
    
stopnie = float(input('Podaj ilosc stopni, ktore chcesz zamienic na radiany (Jesli nie chcesz - wpisz 0) '))
radiany = float(input('Podaj ilosc radianow, ktore chcesz zamienic na stopnie (Jesli nie chcesz - wpisz 0) '))
stop_rad(radiany, stopnie)

