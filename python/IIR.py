# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 21:00:29 2023

@author: juani
"""

##  Filtro IIR a partir de un butter a travez de la bilineal

import scipy as sp
import scipy.signal as sig

import math as m
import numpy as np
import matplotlib.pyplot as plt
from pytc2 import sistemas_lineales
import pytc2.sistemas_lineales as tc2

plt.close('all')

w0=1e3
orden=2

allsys = []
descripciones = []

num,den = sig.butter(orden, w0,btype='low',analog=True)
my_af = tc2.TransferFunction(num,den)




#Creo los sistemas digitales con diferentes fs
for n in [3,10,100]:
    
    fs=w0*n/2/np.pi
    k=fs*2
    numz , denz = sig.bilinear(num, den, fs=k) 
    
    my_df = sig.TransferFunction(numz,denz, dt = 1/fs)
    allsys+=[my_df]
    descripciones+=['Fs = W0 * %d'% n]
    


#       Normalizado respecto al de mayor frecuencia:
#tc2.analyze_sys(allsys, descripciones, xaxis="norm", fs=fs/2)

#       Normalizado individual para cada sistema (visualizo al de mayor fs aplastado contra la izquierda)
#tc2.analyze_sys(allsys, descripciones, xaxis="norm")

#       Frecuencias originales. Sin normalizar. Cortan en fs/2 (con xaxis="frec") o en ws/2 (xaxis="omega")
tc2.analyze_sys(allsys, descripciones)  #Puede observarse que el más fiel al analógico es el de mayor fs

#       Gráfico del analógico original
tc2.bodePlot(my_af,'Analógico')

#Para hacer la comparativa entre analógico y digital
#allsys+=[my_af]
#descripciones+=['Analógico']
#tc2.analyze_sys(allsys, descripciones, xaxis="freq")
























