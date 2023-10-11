# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:12:22 2023

@author: juani
"""
##############################################
# Este archivo es el que hicimos en clase para entender el tp lab de las frecuencias cardiacas y demás
##############################################


# Inicialización e importación de módulos

# Módulos para Jupyter
import warnings
warnings.filterwarnings('ignore')

# Módulos importantantes
import scipy.signal as sig
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio
from pytc2.sistemas_lineales import plot_plantilla


mpl.rcParams['figure.figsize'] = (10,10)
###
## Señal de ECG registrada a 1 kHz, con contaminación de diversos orígenes.
###

# para listar las variables que hay en el archivo
#io.whosmat('ecg.mat')
mat_struct = sio.loadmat('ecg.mat')

ecg_one_lead = mat_struct['ecg_lead']
ecg_one_lead = ecg_one_lead.flatten()
cant_muestras = len(ecg_one_lead)

fs = 1000 # Hz
nyq_frec = fs / 2
w_nyq=2*np.pi*nyq_frec
# Plantilla

# filter design
ripple = 1 # dB
atenuacion = 40 # dB

ws1 = 1.0/nyq_frec #Hz
wp1 = 3.0/nyq_frec #Hz
wp2 = 25.0/nyq_frec #Hz
ws2 = 35.0/nyq_frec #Hz


band_pass = sig.iirdesign([wp1,wp2], [ws1, ws2], ripple, atenuacion, ftype='butter', output='sos')   #poco mejor que iirfilter

#print(band_pass)        # Las columnas que me devuelve son 6 pq son 3 coef "b" y 3 "a"

plt.figure()
plt.cla()

frecuencias = np.linspace(0.5, 100, 1000)

w,h=sig.sosfreqz(band_pass, frecuencias, fs = fs)

db = 20*np.log10(np.maximum(np.abs(h), 1e-5))

plt.plot(w, db, label='band_pass')

plt.ylabel('Amplitud [dB]')

plot_plantilla(filter_type = 'bandpass' , fpass = [3,25], ripple = ripple , fstop = [1,35], attenuation = atenuacion, fs = fs)


ECG_f_butt = sig.sosfilt(band_pass, ecg_one_lead)

demora = 750


# Segmentos de interés con ALTA contaminación

regs_interes = ( 
        np.array([5, 5.2]) *60*fs, # minutos a muestras
        np.array([12, 12.4]) *60*fs, # minutos a muestras
        np.array([15, 15.2]) *60*fs, # minutos a muestras
        )


fig_sz_x = 10
fig_sz_y = 7
fig_dpi = 100 # dpi

fig_font_size = 16

mpl.rcParams['figure.figsize'] = (fig_sz_x,fig_sz_y)
plt.rcParams.update({'font.size':fig_font_size})


for ii in regs_interes:
    
    # intervalo limitado de 0 a cant_muestras
    zoom_region = np.arange(np.max([0, ii[0]]), np.min([cant_muestras, ii[1]]), dtype='uint')
    
    plt.figure(figsize=(fig_sz_x, fig_sz_y), dpi= fig_dpi, facecolor='w', edgecolor='k')
    plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', linewidth=2)
    plt.plot(zoom_region, ECG_f_butt[zoom_region], label='Butter')
    #plt.plot(zoom_region, ECG_f_win[zoom_region + demora], label='Win')
    
    plt.title('ECG filtering example from ' + str(ii[0]) + ' to ' + str(ii[1]) )
    plt.ylabel('Adimensional')
    plt.xlabel('Muestras (#)')
    
    axes_hdl = plt.gca()
    axes_hdl.legend()
    axes_hdl.set_yticks(())
            
    plt.show()











