def geringoso(lista):
    global diccionario
    palabraNueva = ""
    for palabra in lista:
        for caracter in palabra:
            if caracter == "a" or caracter == "á":
                palabraNueva = palabraNueva + "apa"
            elif caracter == "e" or caracter == "é":
                palabraNueva = palabraNueva + "epe"
            elif caracter == "i" or caracter == "í":
                palabraNueva = palabraNueva + "ipi"
            elif caracter == "o" or caracter == "ó":
                palabraNueva = palabraNueva + "opo"
            elif caracter == "u" or caracter == "ú":
                palabraNueva = palabraNueva + "upu"
            else:
                palabraNueva = palabraNueva + caracter

        diccionario[palabra] = palabraNueva
        palabraNueva = ""


diccionario = {}
lista = ('naranja','manzana','banana')
geringoso(lista)

print(diccionario)
