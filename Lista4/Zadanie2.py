def wywalanie(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

lista = [1,5,1,17,1,5,1]
print(wywalanie(lista))