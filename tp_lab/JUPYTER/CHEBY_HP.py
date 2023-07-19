#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 19:23:53 2023

@author: juani
"""

#%% Librerías externas NumPy, SciPy y Matplotlib
from scipy import signal as sig  
import matplotlib.pyplot as plt               #le doy un nombre (plt) al matplotlib para usarlo más comodamente
import numpy as np                            #le doy un nombre (np) al numpy para usarlo más comodamente
import math as m

import pandas as pd

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

# Defino mi plantilla pasa altos

fs=1200
fp=4600
a_MAX=1
a_min=20

ws=fs*2*m.pi
wp=fp*2*m.pi

wp_n=1      # wp/wp
ws_n=ws/wp

#Defino mi plantilla pasa bajos prototipo

zp_n=1
zs_n=1/ws_n

print("Frecuencia paso LP:",zp_n)
print("Frecuencia stop LP:",zs_n)
#%%

# Averiguo epsilon y 'n'

eps = m.sqrt(10**(a_MAX/10)-1)
n , z3db = sig.cheb1ord(zp_n, zs_n, a_MAX, a_min, True)
print("Epsilon: ", eps)
print("Orden: ", n)

#%%

# Diseño de cheby con esos parámetros

z,p,k = sig.cheb1ap(n, a_MAX)
LP_SOS = sig.zpk2sos(z, p, k)

print_subtitle('TRANSFERENCIA PASA BAJOS PROTOTIPO')

tc2.pretty_print_SOS(LP_SOS)

#%%

# Transformo mi pasa bajos a pasa altos

num_lp , den_lp = sig.zpk2tf(z, p, k)

num_hp , den_hp = sig.lp2hp(num_lp, den_lp)

HP_SOS = sig.tf2sos(num_hp, den_hp)

print_subtitle('TRANSFERENCIA PASA ALTOS')

tc2.pretty_print_SOS(HP_SOS)

#%%

# Corro los gráficos para verificar las condiciones de plantilla

H1 = sig.TransferFunction(num_hp, den_hp)
plt.close('all')
tc2.analyze_sys(H1)


#%%

#Extraigo los datos del archivo que me da el analizador

data1 = pd.read_csv('MODULO.csv', delimiter=',')
data2 = pd.read_csv('FASE.csv', delimiter=',')

data1_frec = data1['Frec']
data1_mod = data1['Volt']

data2_frec = data2['Frec']
data2_fase = data2['Fase']

fig, (ax1,ax2) = plt.subplots(2, 1, sharex=True)

markers_on = [4600]

ax1.semilogx(data1_frec, data1_mod)
ax1.grid(True)
ax1.minorticks_on()
# Customize the major grid
ax1.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')



ax2.semilogx(data2_frec, data2_fase)
ax2.grid(True)
ax2.minorticks_on()
# Customize the major grid
ax2.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
ax2.grid(which='minor', linestyle=':', linewidth='0.5', color='black')































