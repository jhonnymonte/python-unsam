import csv
from pprint import pprint

camiones = []
precios = 0.0


def leer_camion(nombre_archivo):

    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        for row in rows:  # creo el diccionario en base al archivo
            d = {'nombre': row[0],
                 'cajones': int(row[1]),
                 'precio': float(row[2])}
            camion.append(d)  # paso el diccionario a la lista de camion
        return camion


camion = leer_camion('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/camion.csv')
#precios=leer_precios('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/precios.csv')

pprint(camion)
# pprint(precios)
