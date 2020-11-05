def konwersja_rgb_hsv(r, g, b):
    r /= 250
    g /= 250
    b /= 250
    
    maks = max(r, g, b)
    mini = min(r, g ,b)
    roznica = maks - mini
    
    if(maks == mini):
        h = 0
    elif(maks == r):
        h = (60 * ((g - b) / roznica) + 360) % 360
    elif(maks == g):
        h = (60 * ((b - r) / roznica) + 120) % 360
    elif(maks == b):
        h = (60 * ((r - g) / roznica) + 240) % 360
    
    if(maks == 0):
        s = 0
    else:
        s = (roznica/maks) * 100
    
    v = maks *100
    
    print(str(h) + ', ' + str(s) + ', ' + str(v))
    


a = int(input('Podaj r: '))
b = int(input('Podaj g: '))
c = int(input('Podaj b: '))

konwersja_rgb_hsv(a, b, c)
