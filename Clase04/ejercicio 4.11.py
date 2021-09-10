#autor: Jonatan Montenegro
#Email: mrmontenegro@gmail.com
import csv
f=open('C:/Users/User2021/Documents/python/unsam/archivos/Data/fecha_camion.csv')
rows=csv.reader(f)
headers=next(rows)
select = ['nombre', 'cajones', 'precio']
indices = [headers.index(ncolumna) for ncolumna in select]

row = next(rows)
record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}

camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]













