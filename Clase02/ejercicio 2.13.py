import csv
with open('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/camion.csv', 'rt') as f:
    filas= csv.reader(f)
    next(filas)
    fila=next(filas)

    
    d={
        'nombre' : fila[0],
        'cajones' : int(fila[1]),
        'precio'  : float(fila[2])
    }
    print(d)
    
    d['fecha'] =(14,8,2020)
    d['cuenta'] = (12345)

    print (d)

    for k in d:
        print('k=',k)

    for k in d:
        print(k, '=', d[k])

    claves = d.keys()
    claves = d.values()
    print (claves)