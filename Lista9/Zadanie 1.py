import numpy as n

a = n.array([[1,2,3,-2,-1], [3,5,5,-3,-9], [2,3,2,0,-8], [2,6,7,-5,1], [1,2,6,-4,10]])
b = n.array([6,2,-5,17,12])

x = n.linalg.solve(a,b)
print(x)