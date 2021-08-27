#autor: Jonatan Montenegro
#Email: mrmontenegro@gmail.com

#No estoy seguro del correcto funcionamiento de este ejercicio. no logre verificarlo, aguardo comentarios sobre alguna falla.


import csv
import sys
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
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)