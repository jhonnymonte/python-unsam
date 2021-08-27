#autor: Jonatan Montenegro
#Email: mrmontenegro@gmail.com

def buscar_precio(fruta):
#para la verificacion correcta el ejercicio la persona que lo corrija seguramente debe modificar el directorio raiz del archivos precios.csv
    f = open('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/precios.csv',
             'rt', encoding='utf8')
    mensaje=''        
    for lines in f:#recorro el archivo
        try:# realizo el try/excepto para corregir la falta de datos en el archivo
            columna = lines.split(',')
            producto_solicitado = str(columna[0])
            precio = float(columna[1])
            if fruta == producto_solicitado:
                mensaje=(f'el precio de la {fruta} es de {precio}')
                return mensaje
        except IndexError:# hago la excepcion del error y indico el mensaje
            return(f'{fruta} no figura en la lista de precios')
            
    mensaje=(f'{fruta} no figura en la lista de precios')
    f.close()
    return mensaje

#comandos de verificacion    
precio = buscar_precio('Lima')
print(precio)
precio = buscar_precio('Anana')
print(precio)


















