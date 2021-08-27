import csv
from collections import Counter
from pprint import pprint
#%% ejercicio 3.18
def leer_parque(nombre_archivo,parque):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        lista = []
        try:
            for n_fila, fila in enumerate(filas, start=1):
                record = dict(zip(encabezado, fila))
                if parque==record['espacio_ve']:
                    lista.append(record)                 
                else:
                    pass               
        except ValueError:
            print(f'Fila {n_fila}: Error en lectura de datos: {fila}\n')
    return lista

gral_paz=leer_parque('C:/Users/User2021/Documents/python/unsam/archivos/Data/arbolado-en-espacios-verdes.csv','GENERAL PAZ')
print(len(gral_paz))

#%% ejercicio 3.19
def especies(lista_arboles):
    lista=[]
    for arbol in lista_arboles:
        lista.append(arbol['nombre_com'])
    return set(lista)
#%% ejercicio 3.20
def contar_ejemplares(lista_arboles):
    d=Counter() #creo un contador(que es un diccionario)
    for arbol in lista_arboles:
        d[arbol['nombre_com']]+=1 #a mi diccionario le agrego un mas uno al conteo de especies
    return d

pprint(contar_ejemplares(gral_paz))

#%% ejercicio 3.21
def leer_parque(nombre_archivo,parque):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        lista = []
        try:
            for n_fila, fila in enumerate(filas, start=1):
                registro = dict(zip(encabezado, fila))
                registro['altura_tot']=float(registro['altura_tot'])

                if parque==registro['espacio_ve']:
                    lista.append(registro)                 
                else:
                    pass
                
        except ValueError:
            print(f'Fila {n_fila}: Error en lectura de datos: {fila}\n')
    return lista


gral_paz=leer_parque('C:/Users/User2021/Documents/python/unsam/archivos/Data/arbolado-en-espacios-verdes.csv','GENERAL PAZ')

def obtener_alturas(lista_arboles,especie):
    lista = []
    for arbol in lista_arboles:
        if arbol['nombre_com']==especie:
            lista.append(arbol['altura_tot'])
    return lista
#%%
altura_jac_gral_paz=obtener_alturas(gral_paz,'Jacarandá')
pprint(altura_jac_gral_paz)

# %%
