import random

def sortowanie(x):
    for i in range(len(x)):
        key = x[i]
        j = i-1
        while ((j >= 0) and (x[j] > key)):
            x[i] = x[j]
            x[j] = key
            j -= 1
            i -= 1
    return x

list1 = [random.randint(1,20) for _ in range(100)]
list2 = [random.randint(1,20) for _ in range(200)]
list3 = [random.randint(1,20) for _ in range(300)]


print(sortowanie(list1))
print(sortowanie(list2))
print(sortowanie(list3))