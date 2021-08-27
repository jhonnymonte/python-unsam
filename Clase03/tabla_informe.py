# autor: Jonatan Montenegro
#Email: mrmontenegro@gmail.com
# %%
import csv
from pprint import pprint
totalcompra = 0
camiones = []
precios = 0.0


def leer_camion(nombre_archivo):

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        camion = []
        try:
            for n_fila, fila in enumerate(filas, start=1):
                record = dict(zip(encabezado, fila))
                record['precio'] = float(record['precio'])
                record['cajones'] = int(record['cajones'])

                camion.append(record)
        except ValueError:
            print(f'Fila {n_fila}: Error en lectura de datos: {fila}\n')
    return camion


# %%


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
# %%


def balance(leer_camion, leer_precios):
    camion = leer_camion
    costoCamion = 0
    Venta = 0

    for aux in camion:
        costoCamion = costoCamion + aux['cajones'] * aux['precio']
        Venta = Venta+leer_precios[aux['nombre']]*aux['cajones']
        resultado = (Venta-costoCamion)
        mensaje = (
            f'el valor de compra del producto fue de:{costoCamion:0.2f} el total de venta:{Venta:0.2f} la ganancia es de:{resultado:0.2f}')

    return mensaje

# %%


def hacer_informe(leer_camion, leer_precios):
    '''Recibe la lista de cajones, un diccionario con precio y devuelve una lista de tuplas con la información obtenida'''
    informe_nombres = []
    informe_cajones = []
    informe_precios = []
    informe_cambio = []
    informe_camion = ()
    signopesos = []
    for i, fila in enumerate(leer_camion, start=1):
        informe_nombres.append(fila['nombre'])
        informe_precios.append(fila['precio'])
        informe_cajones.append(fila['cajones'])
        for i, fila2 in enumerate(leer_precios, start=1):
            if fila['nombre'] in fila2['nombre']:
                informe_cambio.append(
                    round((fila2['precio'] - fila['precio']), 2))

    for n in informe_precios:
        signopesos.append('$'+str(n))

    informe_camion = tuple(
        zip(informe_nombres, informe_cajones, signopesos, informe_cambio))
    return informe_camion


camion = leer_camion(
    '../Data/camion.csv')
precios = leer_precios(
    '..Data/precios.csv')
# resultado=balance(camion,precios)
informe = hacer_informe(camion, precios)
pprint(informe)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(
    f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('---------- ---------- ---------- ----------')
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')


# pprint(precios)

# pprint(camion)

# print(resultado)
