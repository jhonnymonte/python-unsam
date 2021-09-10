import random
import numpy as np
#import matplotlib.pyplot as plt

#%% ejercicio 5.10
def crear_album(figus_total):
    return np.zeros(figus_total)
#%% ejercicio 5.11
def album_incompleto(album):
    return 0 in album
#%% ejercicio 5.12
def comprar_figu(figus_total):
    return random.randint(1,figus_total)-1
#%% ejercicio 5.13
def cuantas_figus(figus_total):
    album=crear_album(figus_total)
    while album_incompleto(album):
        album[comprar_figu(figus_total)] +=1
    return album.sum()
cuantas_figus(6)
# %% ejercicio 5.14
figus_total=6
n_repeticiones=1000
l=[]

for i in range(n_repeticiones):
    l.append(cuantas_figus(figus_total))

print(f'para llenar el album de {figus_total}  figuritas compre un promedio de {np.mean(l)} ')

# %% ejercicio 5.15
def experimento_figus(n_repeticiones,figus_total):
    l=[]
    for i in range(n_repeticiones):
        l.append(cuantas_figus(figus_total))
    return np.mean(l)
# %% ejercicio 5.17
def  comprar_paquetes(figus_total,figus_paquete):
    p=[]
    for i in range(figus_paquete):
        p.append(comprar_figu(figus_total))
    return p
    
figus_total=670
figus_paquete=5



# %%
