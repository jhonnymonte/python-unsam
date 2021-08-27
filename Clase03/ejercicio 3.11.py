#autor: Jonatan Montenegro
#Email: mrmontenegro@gmail.com
#%%
import csv
from pprint import pprint

totalcompra = 0
camiones = []
precios = 0.0
import csv
def leer_camion(nombre_archivo):
    
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        camion=[]
        try:
            for n_fila, fila in enumerate(filas, start=1):
                record = dict(zip(encabezado, fila))
                record['precio'] = float(record['precio'])
                record['cajones'] = int(record['cajones'])
                
                camion.append(record)
        except ValueError:
            print(f'Fila {n_fila}: Error en lectura de datos: {fila}\n')
    return camion
    
#%%
import csv
def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        precio_cajones = {}
        for row in rows:
            if row != []:
                precio_cajones[row[0]] = float(row[1])

        return precio_cajones

#%%
def balance(leer_camion,leer_precios):
    camion=leer_camion
    costoCamion=0
    Venta=0

    for aux in camion:
        costoCamion=costoCamion + aux['cajones']* aux['precio']
        Venta=Venta+leer_precios[aux['nombre']]*aux['cajones']
        resultado=(Venta-costoCamion)    
        mensaje=(f'el valor de compra del producto fue de:{costoCamion:0.2f} el total de venta:{Venta:0.2f} la ganancia es de:{resultado:0.2f}')  
    
    return mensaje




#%%
camion = leer_camion('C:/Users/User2021/Documents/python/unsam/archivos/Data/camion.csv')
#precios = leer_precios('C:/Users/User2021/Documents/python/unsam/archivos/Data/precios.csv')
#resultado=balance(camion,precios)

from collections import Counter
tenencias=Counter()
for s in camion:
    tenencias[s['nombre']] += s['cajones']

camion2=leer_camion('C:/Users/User2021/Documents/python/unsam/archivos/Data/camion2.csv')
tenencias2=Counter()
for s in camion2:
    tenencias2[s['nombre']] += s['cajones']








# %%
