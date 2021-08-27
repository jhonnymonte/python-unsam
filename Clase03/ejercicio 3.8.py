
#autor: Jonatan Montenegro
#Email: mrmontenegro@gmail.com
import csv


def costo_Camion(nombre_Archivo):
    with open( nombre_Archivo) as f:
        filas=csv.reader(f)
        encabezados=next(filas)
        fila=next(filas)
        costo_total=0
        for n_fila,fila in enumerate(filas,start=1):
            record=dict(zip(encabezados,fila))
            try:
                ncajones=int(record['cajones'])
                precio=float(record['precio'])
                costo_total += ncajones*precio
                
            except ValueError:
                print(f'Fila{n_fila}:No puede intepretar:{fila}')
        
        return costo_total
        
        
        
    
    

camion=costo_Camion ('C:/Users/User2021/Documents/python/unsam/archivos/Data/missing.csv')

print(camion)