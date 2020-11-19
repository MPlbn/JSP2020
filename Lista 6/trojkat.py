import math

def obw(a,b,c):
    return a+b+c

def pole(a,b,c):
    p = obw(a,b,c) / 2
    wynik = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return wynik

def bok_typ(a,b,c):
    if (a == b and b == c and a == c):
        x = 'Trojkat jest rownoboczny!'
    elif ((a == b and b != c and a != c) or (a != b and b == c and a != c) or (a != b and b != c and a == c)):
        x = 'Trojkat jest rownoramienny'
    else:
        x = 'Trojkat jest roznoboczny'
    return x

def kat(a,b,c):
    pusta = []
    cos_alfa = ((b**2 + c**2 - a**2) / 2*b*c) / 1000
    cos_beta = ((a**2 + c**2 - b**2) / 2*a*c) / 1000
    cos_gamma = ((a**2 + b**2 - c**2) / 2*a*b) / 1000
    
    alfa = (math.acos(cos_alfa) * 360) / (2*math.pi)
    beta = (math.acos(cos_beta) * 360) / (2*math.pi)
    gamma = (math.acos(cos_gamma) * 360) / (2*math.pi)
    
    pusta.append(alfa)
    pusta.append(beta)
    pusta.append(gamma)
    return pusta

def kat_typ(x):
    prost = 0
    rozw = 0
    ostr = 0
    for i  in x:
        if i == 90.0:
            prost += 1
        elif i < 90.0:
            ostr += 1
        elif i > 90.0:
            rozw += 1
    if prost == 1:
        odp = 'Trojkat jest prostokatny'
    else:
        if rozw != 0:
            odp = 'Trojkat jest rozwartokatny'
        else:
            odp = 'Trojkat jest ostrokatny'
    return odp