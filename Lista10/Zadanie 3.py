import itertools as it

class podlisty:
    def __init__(self,x):
        self.x = x
    def wybor(self):
        arr = list(it.combinations(self.x, 3))
        re = []
        for i in arr:
            if((i[0] + i[1] + i[2]) == 0):
                re.append(i)
        return re
        

lista = list(range(-5, 5)) #Tutaj wstawić trzeba listę - do wyboru do koloru
n_lista = podlisty(lista)
print(n_lista.wybor())