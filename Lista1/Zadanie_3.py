import math

a = input() 
b = input() 
alpha = input() 

alpharad = (float(alpha) * 2 * math.pi) / 360
pole = 0.5 * float(a) * float(b) * math.sin(float(alpharad))