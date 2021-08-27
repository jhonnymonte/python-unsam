#Autor Jonatan montenegro
#Contacto mrmontenegro@gmail.com

#%%
#ejercicio 3.1
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        
        if expresion[i] == 'a':
            return True
        else:
            return False
    i +=1 #en este caso lo que corregi es correr el contador dentro del else una identacion para atras que el contador funcione. igualmente no estoy seguro de que sea lo que pide ya que no corre toda la palabra solamente la primera expresion

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#ejercicio 3.2
#%%
def tiene_a(expresion):#coloco ":" para definir la funcion
    n = len(expresion)
    i = 0
    while i<n:#coloco ":" para la condicion del while :
        if expresion[i] == 'a' :#coloco "==" para buscar la igualdad de la expresion y coloco ":"
            return True
        else: #agrego el else del ciclo if
            return False # modifico la identacion y la expresion "false"
    i += 1#cambio de posicion el contador para que quede dentro del while
tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
#ejercicio 3.3

#%%
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')# asigno valor de string a la expresion obtenida de la consola
#ejercicio 4
#%%
def suma(a,b):
    c = a + b
    return c # se agrega el return y la variable a retornar

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#ejercicio 5
#%%
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
        return camion #se que es un problema de asignacion de memoria o superposicion de memoria pero no encontre como solcuionarlo

camion = leer_camion('C:/Users/User2021/Documents/python/unsam/archivos/Data/camion.csv')
pprint(camion)

# %%
