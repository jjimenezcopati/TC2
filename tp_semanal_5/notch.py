#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 19:23:53 2023

@author: juani
"""

#%% Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction     #de el scipy solo exporto la funcion transferfunction
from scipy import signal as sig  
import matplotlib.pyplot as plt               #le doy un nombre (plt) al matplotlib para usarlo más comodamente
import numpy as np                            #le doy un nombre (np) al numpy para usarlo más comodamente
import math as m

##### Librería de TC2
from pytc2.general import print_latex, print_subtitle
import pytc2.sistemas_lineales as tc2 #libreria de la catedra.

#Para graficos

import matplotlib as mpl

fig_sz_x = 13
fig_sz_y = 7
fig_dpi = 80 # dpi
fig_font_size = 16

mpl.rcParams['figure.figsize'] = (fig_sz_x, fig_sz_y)
mpl.rcParams['figure.dpi'] = fig_dpi
mpl.rcParams.update({'font.size':fig_font_size})

#%%
N = 2
wp = 1
num_but, den = sig.butter(N,  wp, btype='low', analog=True) 
num_but = [1/9, 0,1]
H1 = sig.TransferFunction(num_but,den)
tc2.pretty_print_lti(num_but,den)
tc2.analyze_sys(H1,"Notch PB")
#%%
N = 1
wp = 1
num_but, den = sig.butter(N,  wp, btype='low', analog=True) 
H1 = sig.TransferFunction(num_but,den)
tc2.pretty_print_lti(num_but,den)
tc2.analyze_sys(H1,"RC")
#%%
N = 3
wp = 1
num_but, den = sig.butter(N,  wp, btype='low', analog=True) 
num_but= [1/9, 0,1]
H1 = sig.TransferFunction(num_but,den)
tc2.pretty_print_lti(num_but,den)
tc2.analyze_sys(H1,"Filtro full_LP")
#%%
num_hp , den_hp = sig.lp2hp(num_but, den, 1)
H1 = sig.TransferFunction(num_hp,den_hp)
tc2.pretty_print_lti(num_hp,den_hp)
tc2.analyze_sys(H1,"Filtro full_HP")









