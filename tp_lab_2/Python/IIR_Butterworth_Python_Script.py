# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:45:12 2023

@author: talbanesi
"""

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy import signal as sig
from pytc2.sistemas_lineales import analyze_sys, pretty_print_bicuad_omegayq, plot_plantilla

plt.close('all') 

def group_delay(ww, phase):
    
    groupDelay = -np.diff(phase)/np.diff(ww)
    return(np.append(groupDelay, groupDelay[-1]))

# Plantilla
f_pass = 2e3
f_stop = 3e3
at_pass = 1
at_stop = 20
fs = 44e3
f_nyq = fs/2

# Coeficientes
num_iir = np.array([1.5866236489781e-07,1.26929891918248e-06,4.442546217138679e-06,8.885092434277359e-06,1.1106365542846699e-05,8.885092434277359e-06,4.44254621713868e-06,1.26929891918248e-06,1.5866236489781e-07])
den_iir = np.array([1.0,-6.413306608385417,18.12542897301968,-29.465989614914925,30.120651762703893,-19.81618064656616,8.190625602136983,-1.9439664239390542,0.2027775735104071])

w = np.logspace(-4, 4, 1000) / f_nyq * np.pi

_, h = sig.freqz(num_iir, den_iir, w)

w = w / np.pi * f_nyq

# Modulo
#plt.axis([0, 100, -60, 5 ]);
plt.title('Filtros diseñados')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Módulo [dB]')
plt.plot(w, 20 * np.log10(np.abs(h)), label='IIR')
plt.legend('IIR')
plot_plantilla(filter_type = 'lowpass', fpass = f_pass, ripple = at_pass , fstop = f_stop, attenuation = at_stop, fs = fs)

# Fase
plt.figure()
plt.title('Respuesta de fase IIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Ángulo [rad]')
#fase_iir = np.unwrap(np.angle(h))
fase_iir = np.angle(h)
plt.plot(w, fase_iir)
plt.grid(which='both', axis='both')
#plt.xlim(0, 100)
#plt.axis([0, 100, -25, 5 ]);

# Retardo
gd_iir = group_delay(w, fase_iir)
plt.figure()
plt.title('Retardo de grupo IIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Demora [s]')
plt.plot(w,gd_iir)
plt.grid(which='both', axis='both')
#plt.xlim(0, 100)
#plt.axis([0, 100, -2, 7 ]);