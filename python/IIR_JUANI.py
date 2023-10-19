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
for n in [30,50,100]:
    #    Frecuencia de muestreo a partir de múltiplos de f0
    fs= n * w0/2/np.pi
    # La k que se usará para la aplicacion de la bilineal sobre el filtro analog
    k_bilineal=fs*2    
    
    #   w a la que quiero hacer prewarp de ser requerido
    w_prew=w0        
    # Nueva K bilineal que usaré si quiero hacer prewarp
    k_bilineal=2*w_prew/(4*np.tan(w_prew/k_bilineal))
    
    #La k solo la uso para esta conversión. No es mi nueva fs!!!
    numz , denz = sig.bilinear(num, den, fs=k_bilineal) 
    #Uso la fs original y que sigue rigiendo en mi sistema
    my_df = sig.TransferFunction(numz,denz, dt = 1/fs)
    allsys+=[my_df]
    descripciones+=['Fs = W0 * %d'% n]
    


#       Normalizado respecto al de mayor frecuencia:
#tc2.analyze_sys(allsys, descripciones, xaxis="norm", fs=fs/2)

#       Normalizado individual para cada sistema (visualizo al de mayor fs aplastado contra la izquierda)
#tc2.analyze_sys(allsys, descripciones, xaxis="norm")

#       Frecuencias originales. Sin normalizar. Cortan en fs/2 (con xaxis="frec") o en ws/2 (xaxis="omega")
tc2.analyze_sys(allsys, descripciones, xaxis="omega")  #Puede observarse que el más fiel al analógico es el de mayor fs

#       Gráfico del analógico original
tc2.bodePlot(my_af,'Analógico',xaxis="omega")

#Para hacer la comparativa entre analógico y digital
#allsys+=[my_af]
#descripciones+=['Analógico']
#tc2.analyze_sys(allsys, descripciones, xaxis="freq")
























