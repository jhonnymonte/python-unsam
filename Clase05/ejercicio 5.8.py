import random
import numpy as np
#%%
def medir_temp(n):
    temperaturas=[]
    for i in range(n):
        lista=random.normalvariate(37.5,0.2)
        temperaturas.append(lista)
        a=np.array(temperaturas)
        np.save('temperaturas.npy',a)

    return temperaturas
medir_temp(999)




# %%
