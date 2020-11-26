def szyfr(x):
    chartonum = []
    cypher = []
    complete = []
    
    for i in x:
        chartonum.append(ord(i))
    
    for i in chartonum:
        if((i >= 65 and i <= 90) or (i >= 97 and i <= 122)):
            if((i + 4) > 90 and (i + 4) < 97):
                new = i - 90 + 64 + 4
            elif((i + 4) > 122):
                new = i - 122 + 96 + 4
            else:
                new = i + 4
            cypher.append(new)
        else:
            cypher.append(i)
            
    for i in cypher:
        complete.append(chr(i))
    
    return ''.join(complete)
        

def deszyfr(x):
    chartonum = []
    cypher = []
    complete = []

    for i in x:
        chartonum.append(ord(i))

    for i in chartonum:
        if((i >= 65 and i <= 90) or (i >= 97 and i <= 122)):
            if((i - 4) < 65):
                new = i - 4 - 65 + 91
            elif((i - 4) < 97 and (i - 4) > 90):
                new = i - 4 - 97 + 123
            else:
                new = i - 4
            cypher.append(new)
        else:
            cypher.append(i)
            
    for i in cypher:
        complete.append(chr(i))
    
    return ''.join(complete)