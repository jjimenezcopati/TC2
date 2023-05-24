#PASA BAJOS 2do ORDEN
"""


@author: juani
"""

#%% Librerías externas NumPy, SciPy y Matplotlib
import scipy.signal as sig                      #TransferFunction zpf2tf
import matplotlib.pyplot as plt
import numpy as np
import math as m

##### Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

#   Defino unos parámetros posibles para 2 tf

#TF1
phi1=m.pi / 4
qq1 = 2*m.cos(phi1)
w01 = 1

#TF2
phi2=m.pi / 8
qq2 = 2*m.cos(phi2)
w02 = 1

#%% FORMA NO ITERATIVA


#obtengo la tf a partir de numerador y denominador
my_tf1 = sig.TransferFunction( [w01**2], [1, w01/qq1, w01**2] )
my_tf2 = sig.TransferFunction( [w02**2], [1, w02/qq2, w02**2] )

#borra datos anteriores de los plots
plt.close('all')

#bode
bodePlot(my_tf1, fig_id=1, filter_description = 'Q={:3.3f}'.format(qq1) ) #bode tf 1
bodePlot(my_tf2, fig_id=1, filter_description = 'Q={:3.3f}'.format(qq2) ) #bode tf2

#pol y ceros
pzmap(my_tf1, fig_id=2, filter_description = 'Q={:3.3f}'.format(qq) ) #S plane pole/zero plot tf 1
pzmap(my_tf2, fig_id=2, filter_description = 'Q={:3.3f}'.format(qq*2) ) #S plane pole/zero plot tf 2

#retardo de grupo
GroupDelay(my_tf1, fig_id=3, filter_description = 'Q={:3.3f}'.format(qq) )
GroupDelay(my_tf2, fig_id=3, filter_description = 'Q={:3.3f}'.format(qq*2) )


#%% FORMA ITERATIVA

qq_param = [ qq1, qq2 ]
w0_param = [w01,w02]
index = 1


for index in range(len(qq_param)):
    
    
    my_tf = TransferFunction( [w0_param[index]**2], [1, w0_param[index] / qq_param[index], w0_param[index]**2] )
   

    bodePlot(my_tf, fig_id=1, filter_description = 'Q={:3.3f}'.format(qq_param[index]) ) #bode tf 1


    pzmap(my_tf, fig_id=2, filter_description = 'Q={:3.3f}'.format(qq_param[index]) ) #S plane pole/zero plot tf 1


    GroupDelay(my_tf, fig_id=3, filter_description = 'Q={:3.3f}'.format(qq_param[index]) )

    
#%%

z,p,k=sig.tf2zpk(b, a)


















