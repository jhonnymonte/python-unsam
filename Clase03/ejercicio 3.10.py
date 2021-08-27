#%%
precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23
    }


lista_precios=list(zip(precios.values(),precios.keys()))

min(lista_precios)

max(lista_precios)

sorted(lista_precios)

# %%

a = [1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.4, 0.6, 0.8]
list(zip(a, b, c))
# %%
a = [1, 2, 3, 4, 5, 6]
b = ['x', 'y', 'z']
list(zip(a,b))
# %%
