#autor jonatan montenegro
#mrmontenegro@gmail.com

#%%
def buscar_u_elemento(lista,e):
    i=0
    pos =-1
    for i,z in enumerate(lista):
        if z==e:
            pos=i
        i+=1                 
        
    return pos
#%%
def buscar_n_elemento(lista,e):
    contador=0
    for i in lista:
        if i==e:
            contador+=1             
    return contador

# %%
def maximo(lista):
    m=None
    for e in lista:
        if m is None or e > m:
            m=e
    return m




