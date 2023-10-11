# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:00:14 2023

@author: juani
"""

import warnings
warnings.filterwarnings('ignore')

# Módulos importantantes
import scipy.signal as sig
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio
from pytc2.sistemas_lineales import plot_plantilla




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