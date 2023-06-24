#Pasa altos con butter
"""


@author: juani
"""

#%% Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction     #de el scipy solo exporto la funcion transferfunction
from scipy import signal as sig  
import matplotlib.pyplot as plt               #le doy un nombre (plt) al matplotlib para usarlo más comodamente
import numpy as np                            #le doy un nombre (np) al numpy para usarlo más comodamente
import math as m

##### Librería de TC2
 
import pytc2.sistemas_lineales as tc2 #libreria de la catedra. en este caso importo diag. pol. y ceros, retardo y bode
#Defino mi plantilla

alp_MAX=0.5      #dB
alp_min=24      #dB
    

wp_n_pb=1;             # wp/wp
ws_n_pb=2.64;

#Se calculan epsilon y n automatico 

eps = m.sqrt( 10**(alp_MAX/10) - 1 )
[n,w0] = sig.cheb1ord(wp_n_pb, ws_n_pb, alp_MAX, alp_min, analog=True) #devuelve el orden minimo y la w0 de un chebby con (wp, ws, alph_max, alph_min, True para filtro analógico)

print("N=",n)
print("Epsilon=",eps)

#Obtengo los polos de mi filtro CHEBY low pass

z,p,k = sig.cheb1ap(n, alp_MAX) #obtengo los polos
num,den=sig.zpk2tf(z, p, k)     #saco el numerador y denominador del lp
# sos = sig.zpk2sos(z, p, k) #paso intermewdio si quisiera sacar las tf de segundo orden del lp. (hay una forma de obtener el BP a partir de estas)

#Convierto con la función transformación lp2bp ($=Q_bp*(s**2+1)/s)

[num , den] = sig.lp2bp(num, den, 1, 0.2)   #devuelve numerador y denominador de mi BP. Por cada polo en mi lp, tengo 2 polos y un cero en mi BP (se debe a la funcion transformación)
   
                                    
#print("NUM: ",num)
#print("DEN: ", den) #en este caso tengo un denominador de 6to orden

sos = sig.tf2sos(num , den , analog=True)   #lo separo en "second order sistems"



tc2.pretty_print_SOS(sos)
%matplotlib qt5

plt.close('all') 

tc2.analyze_sys(sos, sys_name="BP")    #si le paso un sos, me plotea todos los sos en graficos de bode, pzk, etc. Puedo pasarle otros parámetros...



















