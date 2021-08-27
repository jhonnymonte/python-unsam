import csv
from pprint import pprint
def leer_parque(nombre_archivo,parque):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        arboles = []
        try:
            for n_fila, fila in enumerate(filas, start=1):
                record = dict(zip(encabezado, fila))
                if parque==record['espacio_ve']:
                    arboles.append(record)
                else:
                    pass
                
        except ValueError:
            print(f'Fila {n_fila}: Error en lectura de datos: {fila}\n')
    return arboles


parques=leer_parque(('C:/Users/User2021/Documents/python/unsam/archivos/Data/arbolado-en-espacios-verdes.csv'),'GENERAL PAZ')

pprint(parques)