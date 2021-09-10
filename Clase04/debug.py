def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        
        if expresion[i] == 'a':
            print (True)
        else:
            print (False)
        i+=1

rta = tiene_a ('palabra')
print(rta) 