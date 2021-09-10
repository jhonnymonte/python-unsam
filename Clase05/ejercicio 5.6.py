import random
import numpy as np
#%%
def medir_temp(n):
    temperaturas=[]
    for i in range(n):
        lista=random.normalvariate(37.5,0.2)
        temperaturas.append(lista)
        a=np.array(temperaturas)
        np.save('temperaturas.npy',a)

    return temperaturas
        
# %%
def resumen_temp(lista):
    resultados=[]
    maximo=max(lista)
    minimo=min(lista)
    promedio=sum(lista)/len(lista)
    resultados.append(round(maximo,2))
    resultados.append(round(minimo,2))
    resultados.append(round(promedio,2))
    tupla=(resultados)
    
    return tupla
lista=medir_temp(999)
print(lista)


print(resumen_temp(lista))


        
    



# %%
