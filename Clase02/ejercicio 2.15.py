import csv

def leer_camion(nombre_archivo):

    camion=[]
    total=0.0

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            ncajones = int(row[1])
            precio = float(row[2])
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
        for saldo in camion:
            total += saldo[1]*saldo[2]
        return (total)
    

    


camion = leer_camion('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/camion.csv')
print(camion)
