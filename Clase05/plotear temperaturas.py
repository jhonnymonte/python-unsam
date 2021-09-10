
# autor jonatan montenegro
# mrmontenegro@gmail.com

import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperatura=np.load('../Data/temperaturas.npy')
    plt.hist(temperatura,bins=100)
    plt.show() 