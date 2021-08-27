#El archivo Data/precios.csv contiene una serie de líneas con precios de venta de cajones en el mercado al que va el camión. El archivo se ve así:

#"Lima",40.22
#"Uva",24.85
#"Ciruela",44.85
#"Cereza",11.27
#"Frutilla",53.72
#...
#Escribí un código que abra el archivo Data/precios.csv, busque el precio de la naranja y lo imprima en pantalla.

#>>> f = open('../Data/precios.csv', 'rt')
#...
#>>> f.close()

#El precio de la naranja es:  106.28

f=open('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/camion.csv', 'rt',encoding='utf8')

#se pide la lectura del archivo y se codifica
with open('C:/Users/User2021/Documents/python/unsam/ejercicios python/clase 2/archivos/camion.csv', 'rt',encoding='utf8') as f:
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

      if fruta == 'Naranja':
         preciototal += precio



print("el precio de las naranjas: ",preciototal)
       
       
              




    




f.close()


