#autor jonatan montenegro
#mrmontenegro@gmail.com

#%%
def invertir_lista(lista):
    invertida=[]
    n=len(lista)
    for i in (lista):
        n=n-1
        invertida.append(lista[n])
    return(invertida)
#%%  invertir lista version revision curso
def invertir_lista(lista):
    invertida=[]
    for e in lista:
        invertida=[e]+invertida
    return invertida
    