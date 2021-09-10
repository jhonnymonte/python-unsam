import csv
#leo el archivo y creo encabezados y columnas
f=open('../Data/dowstocks.csv')
rows= csv.reader(f)
headers=next(rows)
row=next(rows)
#determino el valor de cada columna y armo un diccionario con el encabezado y los valores asignados
types=[str, float, str, str, float, float, float, float, int]
converted=[func(val)for func,val in zip(types,row)]
record=dict(zip(headers,converted))

record['name']

record['price']