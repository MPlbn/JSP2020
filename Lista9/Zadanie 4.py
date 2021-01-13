import numpy as n
import matplotlib.pyplot as mplot

objects = ['C','Java','Python','C++','C#','VB','JS','PHP','R','Groovy']
position = n.arange(len(objects))
pop = [17.38,11.96,11.72,7.56,3.95,3.84,2.2,1.99,1.9,1.84]

mplot.bar(position,pop,align='center', alpha=0.5)
mplot.xticks(position,objects)
mplot.ylabel('%')
mplot.title('Popularnosc poszczegolnych jezykow programowania')

mplot.show()