import time as t

def fibo_r(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibo_r(n-1)+fibo_r(n-2)
    
def fibo_i(n):
    elementy = [0,1]
    for i in range(2,n):
        nowy = elementy[i-1] + elementy[i-2]
        elementy.append(nowy)
    return elementy


a = 30
start = t.time()
for i in range(0,a):
    print(fibo_r(i))
koniec = t.time()
print('Program trwal ' + str(koniec-start) + ' s')

start = t.time()    
for i in fibo_i(a):
    print(i)
koniec = t.time()
print('Program trwal ' + str(koniec-start) + ' s')