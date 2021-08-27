#autor: Jonatan Montenegro
#Email: mrmontenegro@gmail.com
#%%
import csv
from pprint import pprint
totalcompra = 0
camiones = []
precios = 0.0
import csv
def leer_camion(nombre_archivo):
    
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        camion=[]
        try:
            for n_fila, fila in enumerate(filas, start=1):
                record = dict(zip(encabezado, fila))
                record['precio'] = float(record['precio'])
                record['cajones'] = int(record['cajones'])
                
                camion.append(record)
        except ValueError:
            print(f'Fila {n_fila}: Error en lectura de datos: {fila}\n')
    return camion
    
#%%

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        lista = []
        listado = csv.reader(f)
        encabezado = ['nombre', 'precio']
        try:
            for i, fila in enumerate(listado, start=1):
                if fila != '':
                    record = dict(zip(encabezado, fila))
                    record['precio'] = float(record['precio'])
                    lista.append(record)
        except KeyError:
            print(f'fila{i}: Error, faltan datos{fila}\n')
        except ValueError:
            print(f'fila{i}: Error, faltan datos{fila}\n')
    return lista

#%%
def balance(leer_camion,leer_precios):
    camion=leer_camion
    costoCamion=0
    Venta=0

    for aux in camion:
        costoCamion=costoCamion + aux['cajones']* aux['precio']
        Venta=Venta+leer_precios[aux['nombre']]*aux['cajones']
        resultado=(Venta-costoCamion)    
        mensaje=(f'el valor de compra del producto fue de:{costoCamion:0.2f} el total de venta:{Venta:0.2f} la ganancia es de:{resultado:0.2f}')  
    
    return mensaje





camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
resultado=balance(camion,precios)




    
pprint(precios)

pprint(camion)

print(resultado)






# %%

