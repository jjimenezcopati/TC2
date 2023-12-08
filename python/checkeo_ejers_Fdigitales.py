# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 23:20:28 2023

@author: juani
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import pytc2.sistemas_lineales as tc2
from pytc2.sistemas_lineales import analyze_sys, group_delay, GroupDelay, pzmap

# Plantilla
f_pass = 2e3
f_stop = 3e3
at_pass = 1
at_stop = 20
fs = 44e3
f_nyq = fs/2

lp_sos_butter = sig.iirdesign(wp = f_pass/f_nyq, ws = f_stop/f_nyq, gpass = at_pass, gstop = at_stop, analog=False, ftype='butter', output='sos') 
b,a = sig.iirdesign(wp = f_pass/f_nyq, ws = f_stop/f_nyq, gpass = at_pass, gstop = at_stop, analog=False, ftype='butter', output='ba')
frecuencias = np.linspace(0, 23000, num = 1000)

w, h = sig.sosfreqz(lp_sos_butter, frecuencias, fs = fs)

modulo = 20*np.log10(abs(h))
fase = np.angle(h)

f = w*(2*np.pi/fs)
retardo = -np.diff(fase)/np.diff(f)
plt.close("all")

#Modulo
plt.figure(1)
plt.plot(w, modulo)
plt.xlabel('Frec [Hz]')
plt.ylabel('dB')
plt.grid()
plt.title('Módulo')
plt.axis([0,6e3,-30,5])
tc2.plot_plantilla(filter_type = 'lowpass', fpass = f_pass, ripple = at_pass, fstop = f_stop, attenuation = at_stop, fs = fs)
plt.show()

#Fase
plt.figure(2)
plt.plot(w, fase)
plt.grid()
plt.axis([0,20e3,-4,4])
plt.title('Fase')
plt.ylabel('Rads')
plt.xlabel('Frec [Hz]')
plt.show()

#Retardo grupo
plt.figure(3)
plt.plot(w[:-1],retardo)
plt.grid()
plt.axis([0,20e3,-30,35])
plt.title('Gr. delay')
plt.ylabel('Rads')
plt.xlabel('Frec [Hz]')
plt.show()

#PZK
zeros, poles, gain = sig.tf2zpk(b,a)

# Grafica el diagrama de polos y ceros

_ , ax = plt.subplots()
ax.set_aspect(1)
circulo = plt.Circle((0,0), radius=1,fill=False)

ax.add_patch(circulo)
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Ceros')
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Polos')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.title('Diagrama de Polos y Ceros')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginaria')
plt.legend()
plt.grid(True)
plt.show()


#print sos antes de distribuir atenuacion
print(lp_sos_butter)


atenuacion = lp_sos_butter[0,0]
lp_sos_butter[0,0:3]=lp_sos_butter[0,0:3]/atenuacion
aten_distribuida = pow(atenuacion,1/4)

lp_sos_butter[0,0:3]=lp_sos_butter[0,0:3]*aten_distribuida
lp_sos_butter[1,0:3]=lp_sos_butter[1,0:3]*aten_distribuida
lp_sos_butter[2,0:3]=lp_sos_butter[2,0:3]*aten_distribuida
lp_sos_butter[3,0:3]=lp_sos_butter[3,0:3]*aten_distribuida

#print sos despues de distribuir atenuacion
print(lp_sos_butter)







