# autor jonatan montenegro
# mrmontenegro@gmail.com

import csv


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
# %% ejercicio 4.16
H = [float(arbol['altura_tot'])
     for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# %% ejercicio 4.17
H_D = [(float(arbol['altura_tot']), float(arbol['diametro']))
       for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

# %% ejercicio 4.18


def medidas_de_especies(especies, arboleda):
    diccionario={especie:[(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']== especie] for especie in especies}
    return diccionario


especies = (['Eucalipto', 'Palo borracho rosado', 'Jacarandá'])
