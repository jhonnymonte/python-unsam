
def buscar_precio(fruta):
#para la verificacion correcta el ejercicio la persona que lo corrija seguramente debe modificar el directorio raiz del archivos precios.csv
    f = open('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/precios.csv',
             'rt', encoding='utf8')
    mensaje=''        
    for lines in f:#recorro el archivo
        try:
            columna = lines.split(',')
            producto_solicitado = str(columna[0])
            precio = float(columna[1])
            if fruta == producto_solicitado:
                mensaje=(f'el precio de la {fruta} es de {precio}')
                return mensaje
        except IndexError:
            return(f'{fruta} no figura en la lista de precios')
            
    mensaje=(f'{fruta} no figura en la lista de precios')
    f.close()
    return mensaje

    
precio = buscar_precio('Lima')
print(precio)
precio = buscar_precio('Anana')
print(precio)


















