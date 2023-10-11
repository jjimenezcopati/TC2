#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ej2 TP5: Filtros digitales

Created on Wed Aug 18 17:56:57 2021

@author: mariano
"""


import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

from pytc2.sistemas_lineales import  analyze_sys, bodePlot

plt.close("all")
#%% Parte numérica 


fs = 2 # Hz (Normalizamos a fs/2 = f_nyq)

# fpw = w0*np.pi*fs/np.tan(np.pi/2*w0); 

#Defino las frecuencias de muestreo para las que samplearé mi filtro analogico

allfs = np.array([ 100000, 10000 ])
#A mayor frecuencia de muestreo, debería ver que mi forma de filtro digital
#se irá comprimiendo contra la izquierda

#Defino los parámetros que rigen mi sistema analog
W0=1000
Q =np.sqrt(2)/2

# Formo mi transferencia analógica pasa bajos
num = [0,0,W0**2]
den = [1,W0/Q,W0**2]

my_af = sig.TransferFunction(num, den)


all_sys = []
all_sys_desc = []

plt.close('all')

#Hago el sample para las diferentes fs
for this_fs in allfs:
#normalizo respecto a fs
    k = 2 * this_fs #desnormalizada
    W=W0
    
#pongo las expresiones que hallé en papel del numz y denz
    numz =  W0**2 * np.array([1, 2, 1])
    denz =  np.array([(k**2+k*W/Q+W**2), (2*W**2-2*k**2), (k**2-k*W/Q+W**2)])
        
    my_df = sig.TransferFunction(numz, denz, dt=1/this_fs)
    #bodePlot(my_df, fig_id='1', filter_description='f=%d'% this_fs)    
    all_sys += [my_df]
    all_sys_desc += ['fs={:3.3f}'.format(this_fs)]
       

#%% probar diferentes perspectivas:
    

# Desnormalizado en radianes (default)
analyze_sys(all_sys, all_sys_desc)

# Desnormalizado en Hz
#analyze_sys(all_sys, all_sys_desc, xaxis="freq")

# Normalizado individual de cada sistema
#analyze_sys(all_sys, all_sys_desc, same_figs=False, xaxis="norm")

# Normalizado respecto a fs (Hz)
#analyze_sys(all_sys, all_sys_desc, xaxis="norm", fs=allfs[-1]/2)

#analyze_sys(my_af, same_figs=False)
bodePlot(my_af)

    

    
    