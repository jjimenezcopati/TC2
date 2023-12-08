# -*- coding: utf-8 -*-
"""

@author: juani
"""

# Importacion de librerias
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy import signal as sig
from pytc2.sistemas_lineales import analyze_sys, pretty_print_bicuad_omegayq, plot_plantilla

plt.close('all') 

# Funcion para obtener el retardo de grupo
def group_delay(ww, phase):
    
    groupDelay = -np.diff(phase)/np.diff(ww)
    
    return(np.append(groupDelay, groupDelay[-1]))

# Plantilla
f_pass = 1e3
f_stop = 2e3
at_pass = 1
at_stop = 20
fs = 44e3
f_nyq = fs/2

# Coeficientes
# ORDEN 40 - MINIMO PYFDA
num_fir = np.array([-0.050179654958618175,-0.007232230497245624,-0.006729671092117824,-0.005454664497948991,-0.003357525987325359,-0.00042078646823785727,0.0033445341942376144,0.007890576017605169,0.0131364342837594,0.018968622582374167,0.02523913570501457,0.031779725328537956,0.03839700770268516,0.04488580119084945,0.051042296811244274,0.05666119204866031,0.061552401856943155,0.06554736072424443,0.06850748491905205,0.07032651885189414,0.07094048098981227,0.07032651885189414,0.06850748491905205,0.06554736072424443,0.061552401856943155,0.05666119204866031,0.051042296811244274,0.04488580119084945,0.03839700770268516,0.031779725328537956,0.02523913570501457,0.018968622582374167,0.0131364342837594,0.007890576017605169,0.0033445341942376144,-0.00042078646823785727,-0.003357525987325359,-0.005454664497948991,-0.006729671092117824,-0.007232230497245624,-0.050179654958618175])
den_fir = 1

# Vector de frecuencias
w = np.logspace(-4, 4, 1000) / f_nyq * np.pi

# Respuesta en frecuencia
_, h = sig.freqz(num_fir, den_fir, w)

w = w / np.pi * f_nyq

# Modulo
plt.title('Filtros diseñados')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Módulo [dB]')
plt.plot(w, 20 * np.log10(np.abs(h)), label='FIR')
plt.legend('FIR')
plot_plantilla(filter_type = 'lowpass', fpass = f_pass, ripple = at_pass , fstop = f_stop, attenuation = at_stop, fs = fs)

# Fase
plt.figure()
plt.title('Respuesta de fase FIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Ángulo [rad]')
fase_fir = np.unwrap(np.angle(h))
plt.plot(w, fase_fir)
plt.grid(which='both', axis='both')


# Retardo de grupo
gd_iir = group_delay(w, fase_fir)
plt.figure()
plt.title('Retardo de grupo FIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Demora [s]')
plt.plot(w, gd_iir)
plt.grid(which='both', axis='both')
