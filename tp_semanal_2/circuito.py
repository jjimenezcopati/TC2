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

num = [10]
den=[1,1/3,1]
H1 = sig.TransferFunction(num,den)
tc2.pretty_print_lti(num,den)
tc2.analyze_sys(H1,"LP")








