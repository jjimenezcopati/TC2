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
f_pass = [2e3,8e3]
f_stop = [4e3,6e3]
at_pass = 1
at_stop = 20
fs = 44e3
f_nyq = fs/2

# Coeficientes
# ORDEN 40 - MINIMO PYFDA
num_fir = np.array([-0.011987500035322729  ,                
-0.013208274635586841  ,              
-0.006362678992969658  ,               
-0.00016630584191297334,             
-0.0060615123330977376 ,              
-0.024002019776280178  ,              
-0.035821425360649084  ,              
-0.017079421357370676  ,              
 0.038611566577769214  ,              
 0.10411612849690909   ,              
 0.13068077081083193   ,              
 0.083582385292914924  ,             
-0.025401613337691916  ,           
-0.13775476126202793   ,           
 0.81478994300792429   ,              
-0.13775476126202793   ,              
-0.025401613337691916  ,              
 0.083582385292914924  ,              
 0.13068077081083193   ,              
 0.10411612849690909   ,              
 0.038611566577769214  ,              
-0.017079421357370676  ,              
-0.035821425360649084  ,              
-0.024002019776280178  ,              
-0.0060615123330977376 ,              
-0.00016630584191297334,              
-0.006362678992969658  ,              
-0.013208274635586841  ,              
-0.011987500035322729      ])
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
plot_plantilla(filter_type = 'bandstop', fpass = f_pass, ripple = at_pass , fstop = f_stop, attenuation = at_stop, fs = fs)

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
