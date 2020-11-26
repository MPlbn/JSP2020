import random

def sort_bub(x):
    n = len(x)
    while(n > 1):
        for i in range(len(x) - 1):
            if(x[i] > x[i+1]):
                chwilowa = x[i]
                x[i] = x[i+1]
                x[i+1] = chwilowa
        n -= 1
    return x

list1 = [random.randint(1,20) for _ in range(100)]
list2 = [random.randint(1,20) for _ in range(200)]
list3 = [random.randint(1,20) for _ in range(300)]

print(sort_bub(list1))
print(sort_bub(list2))
print(sort_bub(list3))