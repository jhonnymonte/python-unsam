import csv
from pprint import pprint


def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        rows=csv.reader(f)
        lista={}
        ventas=list()
        for row in rows:
            ventas=0
            if row:
                lista[row[0]]=float(row[1])
                
                
        return 




precios=leer_precios('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/precios.csv')

pprint(precios)