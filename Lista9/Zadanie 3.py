import numpy as n
import matplotlib.pyplot as mplot
wall = 1

t = n.arange(0,wall,0.00001)
g = 9.81
deg = 30 #int(input('Podaj wartosc kata (1 - 90): '))
rad = deg/180 * n.pi

v0 = 10 #int(input('Podaj wartosc predkosci poczatkowej: '))
vx = v0 * n.cos(rad) 
vy0 = v0 * n.sin(rad)
vy = v0 * n.sin(rad) - (g * t)

y = v0 * t * n.sin(rad) - (g/2) * (t ** 2)
ymax = n.max(y) #Maksymalna wysokosc
n.roots(y)
