import itertools as it

class segregator:
    def __init__(self,x):
        self.x = x
    
    def kombi(self):      
        i = 1
        arr = []
        while i <= len(self.x):
            arr.extend(list(it.combinations(self.x, i)))
            i += 1
        return arr

lista = [1,4,7,6]
k_nowa = segregator(lista)
print(k_nowa.kombi())