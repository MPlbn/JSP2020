import numpy as n
import matplotlib.pyplot as mplot
wall = 1

t = n.arange(0,wall,0.001)
g = 9.81
deg = int(input('Podaj wartosc kata (1 - 90): '))
rad = deg/180 * n.pi

v0 = int(input('Podaj wartosc predkosci poczatkowej: '))
vx = v0 * n.cos(rad)
vxl = []
for i in list(range(0, 1000)):
    vxl.append(vx) 
    vy0 = v0 * n.sin(rad)
vy = v0 * n.sin(rad) - (g * t)
x = vx * t
y = v0 * t * n.sin(rad) - (g/2) * (t ** 2)
ymax = n.max(y) #Maksymalna wysokosc


mplot.subplot(3,1,1)
mplot.plot(t,vy,t,vxl)
mplot.title('wykres prędkosci w czasie')
mplot.subplot(3,1,2)
mplot.plot(t,y)
mplot.title('wykres położenia w czasie')
mplot.subplot(3,1,3)
mplot.plot(x,y)
mplot.title('wykres toru rzutu')