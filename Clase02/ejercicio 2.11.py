import csv

with open('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/camion.csv', 'rt') as f:
    filas= csv.reader(f)
    next(filas)
    fila=next(filas)

    t=(fila[0],int(fila[1]),float(fila[2]))
    print(t)

    costo=t[1]*t[2]
    print (costo)