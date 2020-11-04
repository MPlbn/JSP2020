def warunek(a):
    lista_parzystych = []
    for i in a:
        x = []
        for cyfra in str(i):
            if (int(cyfra)%2 == 0):
                x.append(cyfra)
        if (x == list(str(i))):
            lista_parzystych.append(i)
    print(lista_parzystych)
            
przedzial = list(range(100,401))
warunek(przedzial)




