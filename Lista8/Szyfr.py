def szyfr(x,y):
    chartonum = []
    cypher = []
    complete = []
    
    for i in x:
        chartonum.append(ord(i))
    
    for i in chartonum:
        if((i >= 65 and i <= 90) or (i >= 97 and i <= 122)):
            if((i + y) > 90 and (i + y) < 97):
                new = i - 90 + 64 + y
            elif((i + y) > 122):
                new = i - 122 + 96 + y
            else:
                new = i + y
            cypher.append(new)
        else:
            cypher.append(i)
            
    for i in cypher:
        complete.append(chr(i))
    
    return ''.join(complete)
        

def deszyfr(x,y):
    chartonum = []
    cypher = []
    complete = []

    for i in x:
        chartonum.append(ord(i))

    for i in chartonum:
        if((i >= 65 and i <= 90) or (i >= 97 and i <= 122)):
            if((i - y) < 65):
                new = i - y - 65 + 91
            elif((i - y) < 97 and (i - y) > 90):
                new = i - y - 97 + 123
            else:
                new = i - y
            cypher.append(new)
        else:
            cypher.append(i)
            
    for i in cypher:
        complete.append(chr(i))
    
    return ''.join(complete)