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
r1=0.1
r2=3
r3=1
c=1

K=r3/r1
w0=1/(r3*c)
Q=r2/r3

num = [K*w0**2]
den=[1,w0/Q,w0**2]
H1 = sig.TransferFunction(num,den)
tc2.pretty_print_lti(num,den)
tc2.analyze_sys(H1,"LP")

#%%
r1=1
r2=1.414
r3=1
c=1

K=r3/r1
w0=1/(r3*c)
Q=r2/r3

num = [K*w0**2]
den=[1,w0/Q,w0**2]
H1 = sig.TransferFunction(num,den)
tc2.pretty_print_lti(num,den)
tc2.analyze_sys(H1,"butter")

#%%
r1=0.1
r2=3
r3=1
c=1

K=r2/r1
w0=1/(r3*c)
Q=r2/r3

num = [K*w0/Q, 0]
den=[1,w0/Q,w0**2]
H1 = sig.TransferFunction(num,den)
tc2.pretty_print_lti(num,den)
tc2.analyze_sys(H1,"BP")





