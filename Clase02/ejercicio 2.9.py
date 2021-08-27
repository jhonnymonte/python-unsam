import csv

def costo_camion(nombre_archivo):
    with open (nombre_archivo, 'rt') as f:
        headers=next(f)
       
        rows=csv.reader(f)
        
        precioTotal=0
        
        try:
            for columna in rows:
                cajones = float(columna[1])
                precio = float(columna[2])
                precioTotal+=round(cajones*precio)
                
            return (round(precioTotal,2))
        except ValueError:
            print("archivo con datos invalidos por favor verifique")

costo = costo_camion('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/camion.csv')
print(costo)