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

def medidas_de_especies(especies, arboleda):
    diccionario = {especie: [(float(arbol['altura_tot']), float(arbol['diametro']))
                            for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return diccionario

especies = (['Eucalipto', 'Palo borracho rosado', 'Jacarandá'])


#def scatter_especies_definidas():
os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)





