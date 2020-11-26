import random

def sortowanie(x):
    for i in range(len(x) - 1):
        key = x[i]
        j = i-1
        while ((j >= 0) and (x[j] > key)):
            x[i] = x[j]
            x[j] = key
            j -= 1
    return x  

list1 = [random.randint(1,20) for _ in range(100)]
list2 = [random.randint(1,20) for _ in range(200)]
list3 = [random.randint(1,20) for _ in range(300)]

lista = [3,7,1,4,19,2]

print(sortowanie(lista))