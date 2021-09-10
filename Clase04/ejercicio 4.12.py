import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

types = [str, int, float]
types[1](row[1])
types[1](row[1])*types[2](row[2])

r=list(zip(types,row))

converted=[]
for func,val in zip(types,row):
    converted.append(func(val))
    