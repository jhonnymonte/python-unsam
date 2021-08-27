import csv
from pprint import pprint

def leer_precios(archivo):
    with open(archivo, 'rt') as f:
        rows=csv.reader(f)
        lista={}
        for row in rows:
            if row:
                lista[row[0]]=float(row[1])
    return lista




            
precios=leer_precios('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/precios.csv')
pprint(precios)