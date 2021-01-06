import random 

def do3(miesiac,x,y):
    if(miesiac < 10):
        cyfra = x
    else:
        cyfra = y
    return cyfra

def Generator_1_6():
    #data
    r_ur = str(random.randint(1800, 2299))
    m_ur = random.randint(1, 12)
    if(m_ur in [1,3,5,7,8,10,12]):
        d_ur = str(random.randint(1,31))
    elif(m_ur in [4,6,9,11]):
        d_ur = str(random.randint(1,30))
    else:
        d_ur = str(random.randint(1,28))  
    #cyf_x to stringi 
    #wygenerowane pierwsze 2 cyfry
    cyf_1_2 = r_ur[2] + r_ur[3]
    #wygenerowane cyfra 3 
    if(r_ur[1] == '8'):
        cyf_3 = do3(m_ur,'8','9')
    elif(r_ur[1] == '9'):
        cyf_3 = do3(m_ur,'0','1')        
    elif(r_ur[1] == '0'): #jakby generator brał też lata 2800+ to trzeba dołożyć jeszcze jeden warunek
        cyf_3 = do3(m_ur,'2','3')
    elif(r_ur[1] == '1'):
        cyf_3 = do3(m_ur,'4','5')
    else:
        cyf_3 = do3(m_ur,'6','7')
    #wygenerowana cyfra 4
    if(m_ur < 10):
        cyf_4 = str(m_ur)
    else:
        cyf_4 = str(m_ur)[1]
    #wygenerowane cyfry 5 i 6
    if(len(d_ur) == 1):
        cyf_5_6 = '0' + d_ur
    else:
        cyf_5_6 = d_ur    
    final = cyf_1_2 + cyf_3 + cyf_4 + cyf_5_6
    return final

def Generator_7_9():
    final = ''
    for i in range(3):
        final += str(random.randint(0,9))
    return final

def Generator_10():
    return str(random.randint(0,9))

def Generator_11(x):
    cyf_1_10 = 1*int(x[0]) + 3*int(x[1]) + 7*int(x[2]) + 9*int(x[3]) + 1*int(x[4]) + 3*int(x[5]) + 7*int(x[6]) + 9*int(x[7]) + 1*int(x[8]) + 3*int(x[9])
    for i in range(0,10):
        sum_kont = cyf_1_10 + i
        if(sum_kont%10 == 0):
            return str(i)

file = open("PESEL.txt", "w")
for i in range(9):
    pre_pesel = Generator_1_6() + Generator_7_9() + Generator_10()
    pesel = pre_pesel + Generator_11(pre_pesel)
    print(pesel)
    file.write(pesel + ' ')
pre_pesel = Generator_1_6() + Generator_7_9() + Generator_10()
pesel = pre_pesel + Generator_11(pre_pesel)
file.write(pesel)
file.close()