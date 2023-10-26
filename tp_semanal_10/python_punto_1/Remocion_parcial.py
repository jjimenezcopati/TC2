# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 19:21:22 2023

@author: juani
"""

import sympy as sp
import numpy as np
# Ahora importamos las funciones de PyTC2

from pytc2.remociones import remover_polo_dc, remover_polo_jw
from pytc2.dibujar import display, dibujar_puerto_entrada, dibujar_funcion_exc_abajo,  dibujar_elemento_serie, dibujar_elemento_derivacion,  dibujar_tanque_RC_derivacion, dibujar_tanque_RC_serie, dibujar_tanque_RC_derivacion,  dibujar_espacio_derivacion, Capacitor, Resistor, ResistorIEC
from pytc2.general import print_latex, print_subtitle, a_equal_b_latex_s
from IPython.display import display,  Markdown

from pytc2.remociones import remover_valor_en_dc, remover_valor_en_infinito, remover_polo_sigma



s = sp.symbols('s ', complex=True)

ZZ = (s**2 + 6*s + 8)/(1*s**2 + 4*s+ 3)

#Dibyjo el puerto
d = dibujar_puerto_entrada('',
                        voltage_lbl = ('+', '$V$', '-'), 
                        current_lbl = '$I$')
#Dibujo la func excitación
d, zz_lbl = dibujar_funcion_exc_abajo(d, 
                 'Z(s)',  
                 ZZ, 
                 hacia_salida = True,
                 k_gap_width = 0.5)
#
d = dibujar_elemento_serie(d,ResistorIEC,'Z_1')
d = dibujar_tanque_RC_derivacion(d,sym_R_label='R_1', capacitor_lbl='C_1')
d = dibujar_elemento_serie(d,ResistorIEC,'Z_2')
d = dibujar_tanque_RC_derivacion(d,sym_R_label='R_2', capacitor_lbl='C_2')
d = dibujar_espacio_derivacion(d)
d = dibujar_elemento_derivacion(d,ResistorIEC,'Z_3')
display(d)

#Guardo raíces de num y den

roots_num = np.roots([1, 6, 8])
print(roots_num)

roots_den = np.roots([1, 4, 3])
print(roots_den)



#Remuevo parcialmente el k_inf

ZZ_2, Z1 = remover_valor_en_infinito(ZZ,sigma_zero=-6)
ZZ_2_exp = sp.expand(ZZ_2)
ZZ_2_exp = sp.simplify(ZZ_2_exp)


print_latex(a_equal_b_latex_s(a_equal_b_latex_s('Z_2', ZZ_2_exp)[1:-1],ZZ_2))
print_latex(a_equal_b_latex_s(a_equal_b_latex_s('k_\infty','Z1')[1:-1],Z1))


YY_2 = 1/ZZ_2
YY_3, Z_RC1, R1, C1=remover_polo_sigma(YY_2,sigma = -6 , isImpedance = False, isRC = True )
YY_3_exp = sp.simplify(YY_3)

print_latex(a_equal_b_latex_s('Y_3',YY_3))
print_latex(a_equal_b_latex_s('Z_{RC1}',Z_RC1))
print_latex(a_equal_b_latex_s('R_1',R1))
print_latex(a_equal_b_latex_s('C_1',C1))

ZZ_3 = 1/YY_3
ZZ_4, Z2 = remover_valor_en_infinito(ZZ_3,sigma_zero=-7/2)
ZZ_4_exp = sp.expand(ZZ_4)
ZZ_4_exp = sp.simplify(ZZ_4_exp)
ZZ_4_exp = sp.collect(ZZ_4,s)

print_latex(a_equal_b_latex_s('Z_4', ZZ_4_exp))
print_latex(a_equal_b_latex_s(a_equal_b_latex_s('k_\infty','Z2')[1:-1],Z2))


YY_4 = 1/ZZ_4
YY_5, Z_RC2, R2, C2=remover_polo_sigma(YY_4,sigma = -3.5 , isImpedance = False, isRC = True )
YY_5_exp = sp.simplify(YY_5)

print_latex(a_equal_b_latex_s('Y_5',YY_5))
print_latex(a_equal_b_latex_s('Z_{RC2}',Z_RC2))
print_latex(a_equal_b_latex_s('R_2',R2))
print_latex(a_equal_b_latex_s('C_2',C2))

YY_5 = 0.797619
Z3 = 1/YY_5

print_latex(a_equal_b_latex_s(a_equal_b_latex_s('Z_5','Z3')[1:-1], Z3))

#Dibyjo el puerto
d = dibujar_puerto_entrada('',
                        voltage_lbl = ('+', '$V$', '-'), 
                        current_lbl = '$I$')
#Dibujo la func excitación
d, zz_lbl = dibujar_funcion_exc_abajo(d, 
                 'Z(s)',  
                 ZZ, 
                 hacia_salida = True,
                 k_gap_width = 0.5)
#Redondeo para que me entre en el gráfico
Z1=round(Z1,3)
Z2=round(Z2,3)
Z3=round(Z3,3)
R1=round(R1,3)
R2=round(R2,3)
C1=round(C1,3)
C2=round(C2,3)
#Dibujo la red
d = dibujar_elemento_serie(d,Resistor,Z1)
d = dibujar_tanque_RC_derivacion(d,sym_R_label=R1, capacitor_lbl=C1)
d = dibujar_elemento_serie(d,Resistor,Z2)
d = dibujar_tanque_RC_derivacion(d,sym_R_label=R2, capacitor_lbl=C2)
d = dibujar_espacio_derivacion(d)
d = dibujar_elemento_derivacion(d,Resistor,'1.255') #no sé por qué no me tomaba Z3
display(d)



















