class Kolo:
    def __init__(self, r):
        self.r = r
    def pole(self):
        return self.r*self.r
    def obw(self):
        return 4*self.r
    
k = Kolo(5)
print(k.obw())
print(k.pole())