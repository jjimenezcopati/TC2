#PASA BAJOS 2do ORDEN
"""


@author: juani
"""

#%% Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


##### Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot


w0 = 1
qq = np.sqrt(2)/2

#%% FORMA NO ITERATIVA

my_tf = TransferFunction( [w0**2], [1, w0/qq, w0**2] )
my_tf2 = TransferFunction( [w0**2], [1, w0/(qq*2), w0**2] )

plt.close('all')

bodePlot(my_tf, fig_id=1, filter_description = 'Q={:3.3f}'.format(qq) ) #bode tf 1
bodePlot(my_tf2, fig_id=1, filter_description = 'Q={:3.3f}'.format(qq*2) ) #bode tf2

pzmap(my_tf, fig_id=2, filter_description = 'Q={:3.3f}'.format(qq) ) #S plane pole/zero plot tf 1
pzmap(my_tf2, fig_id=2, filter_description = 'Q={:3.3f}'.format(qq*2) ) #S plane pole/zero plot tf 2

GroupDelay(my_tf, fig_id=3, filter_description = 'Q={:3.3f}'.format(qq) )
GroupDelay(my_tf2, fig_id=3, filter_description = 'Q={:3.3f}'.format(qq*2) )


#%% FORMA ITERATIVA

qq_param = [ np.sqrt(2)/2 , np.sqrt(2) ]
index = 1;

for index in range(len(qq_param)):
    
    my_tf = TransferFunction( [w0**2], [1, w0/qq_param[index], w0**2] )
   

    bodePlot(my_tf, fig_id=1, filter_description = 'Q={:3.3f}'.format(qq_param[index]) ) #bode tf 1


    pzmap(my_tf, fig_id=2, filter_description = 'Q={:3.3f}'.format(qq_param[index]) ) #S plane pole/zero plot tf 1


    GroupDelay(my_tf, fig_id=3, filter_description = 'Q={:3.3f}'.format(qq_param[index]) )

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    