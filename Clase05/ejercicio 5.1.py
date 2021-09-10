import random

def tirar(Cdados):
    tirada=[]
    for _ in range(Cdados):
        tirada.append(random.randint(1,6))

    return tirada   
def es_generala(tirada):
    return max(tirada)==min(tirada)


