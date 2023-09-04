# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:00:29 2023

@author: juani
"""

##  Filtro pasa altos IIR

import scipy as sp
import math as m
import numpy as np
import matplotlib.pyplot as plt
from pytc2 import sistemas_lineales

plt.close('all')

# %matplotlib qt5

num = [1,0,0]
den = [1,np.sqrt(2),1]
fs=1    #frec de muestreo normalizada

filtro_analogico = sp.signal.TransferFunction(num, den)

numz, denz = sp.signal.bilinear(num, den, fs=1) #convierto el num y den de laplace a Z con la bilinear

#print(np.roots(denz)) #raíces del digital

filtro_digital = sp.signal.TransferFunction(numz, denz, dt=1/fs) #Si aclaro el dt (tiempo de muestreo) lo tomará como filtro digital

#sistemas_lineales.analyze_sys(filtro_digital, 'DIGITAL') #si quiero ver graficas del digital
#sistemas_lineales.analyze_sys(filtro_analogico, 'ANALOGICO') #si quiero ver graficas del analógico