

def costo_camion(nombre_archivo):

    f=open('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/camion.csv', 'rt')
    headers=next(f)
    headers

    precioTotal=0
    cajones=0
    precio=0

    for line in f:
        columna= line.split(',')
        cajones= int(columna[1])
        precio=float(columna[2])
        precioTotal +=(cajones*precio)
        
    return(round(precioTotal,2))

    
    
        

costo = costo_camion('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/camion.csv')
print('Costo total:', costo)

