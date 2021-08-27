#autor: Jonatan Montenegro
#Email: mrmontenegro@gmail.com

import csv
from pprint import pprint
totalcompra = 0
camiones = []
precios = 0.0


def leer_camion(nombre_archivo):

    camion = []

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        for row in rows:  # creo el diccionario en base al archivo
            d = {'nombre': row[0],
                 'cajones': int(row[1]),
                 'precio': float(row[2])}
            camion.append(d)  # paso el diccionario a la lista de camion
        return camion


def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        precio_cajones = {}
        for row in rows:
            if row != []:
                precio_cajones[row[0]] = float(row[1])
    return precio_cajones

def balance(leer_camion,leer_precios):
    camion=leer_camion
    costoCamion=0
    Venta=0

    for aux in camion:
        costoCamion=costoCamion + aux['cajones']* aux['precio']
        Venta=Venta+leer_precios[aux['nombre']]*aux['cajones']
        resultado=(Venta-costoCamion)    
        mensaje=(f'el valor de compra del producto fue de:{costoCamion:0.2f}el total de venta:{Venta:0.2f} la ganancia es de:{resultado:0.2f}')  
    
    return mensaje


camion = leer_camion('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/camion.csv')
precios = leer_precios('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/precios.csv')
resultado=balance(camion,precios)

print(resultado)
