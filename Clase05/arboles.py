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
# %% ejercicio 4.18
def medidas_de_especies(especies, arboleda):
    diccionario = {especie: [(float(arbol['altura_tot']), float(arbol['diametro']))
                             for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return diccionario


especies = (['Eucalipto', 'Palo borracho rosado', 'Jacarandá'])
#%% ejercicio 5.25
os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(
    'C:/Users/User2021/Documents/python/unsam/archivos/Data/arbolado-en-espacios-verdes.csv')
altos = [H]
plt.hist(altos, bins=25)

# %% ejercicio 5.26
h = np.array([H])
d = np.array([D])
x = d
y = h

plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
N = 3255
colors = np.random.rand(N)
area = (10 * np.random.rand(N))**4  # 0 to 15 point radii

plt.scatter(x, y, alpha=0.5, c=colors,cmap='nipy_spectral')
plt.show()

