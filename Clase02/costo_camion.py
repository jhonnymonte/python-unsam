
#autor: Jonatan Montenegro
#Email: mrmontenegro@gmail.com



#se pide la lectura del archivo y se codifica
with open('../Data/camion.csv', 'rt',encoding='utf8') as f:
#creo un salto de lectura para que no lea los titulos de las columnas
   headers=next(f).split(',')
#asigno variable cero para el calculo del total
   preciototal=0
#creo ciclo for para recorrer el chivo
   for lines in f:
       columna= lines.split(',') #creo la lista de columnas en base a las , entre cada coma se define una columna
       fruta = str(columna[0])
       cajones=int(columna[1])
       precio=float(columna[2])
       preciototal +=(cajones*precio)
       

print('el costo total es:',preciototal)
    
    

