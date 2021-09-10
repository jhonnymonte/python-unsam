# autor jonatan montenegro
# mrmontenegro@gmail.com

import csv
import os
import matplotlib.pyplot as plt
import numpy as np


def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        encabezado = next(rows)
        arboleda = []
        types = [float, float, int, float, float, float, int,
                 str, str, str, str, str, str, str, str, float, float]
        try:
            for row in rows:
                converted = [func(val) for func, val in zip(types, row)]
                record = dict(zip(encabezado, converted))
                arboleda.append(record)

        except ValueError:
            print(f'Fila {row}: Error en lectura de datos: {rows}\n')
    return arboleda


arboleda = (leer_arboles(
    'C:/Users/User2021/Documents/python/unsam/archivos/Data/arbolado-en-espacios-verdes.csv'))
# %% altura
H = [float(arbol['altura_tot'])
     for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
# %%  diametro
D = [float(arbol['diametro'])
     for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
#%% altura y diametro de jacaranda
alt_diam_jac=[(arbol['altura_tot'],float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
print(alt_diam_jac)



# %% ejercicio 4.18
def medidas_de_especies(especies, arboleda):
    diccionario = {especie: [(float(arbol['altura_tot']), float(arbol['diametro']))
    for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return diccionario


especies = (['Eucalipto', 'Palo borracho rosado', 'Jacarandá'])
#%% ejercicio 5.25
nombre_archivo=os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
altos = [float(arbol['altura_tot'])
     for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
plt.hist(altos, bins=25)

# %% ejercicio 5.26
def scatter_hd(lista_de_pares):
    pares=np.array(lista_de_pares)
    h=np.array(pares)[:,0]
    d=np.array(pares)[:,1]
    plt.xlim(0,150)
    plt.ylim(0,40)
    plt.scatter(d,h,c=d*h, alpha=.5)
    plt.xlabel("diametro(cm)")
    plt.ylabel("alto(m)")
#%%
scatter_hd(alt_diam_jac)
#%% ejercicio 5.27
os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)

scatter_hd(medidas['Eucalipto'])
scatter_hd(medidas['Palo borracho rosado'])
scatter_hd(medidas['Jacarandá'])


# %%
