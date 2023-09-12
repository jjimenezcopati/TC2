import sympy as sp

from pytc2.cuadripolos import calc_MAI_impedance_ij, calc_MAI_vtransf_ij_mn, calc_MAI_ztransf_ij_mn
from pytc2.general import print_latex
from IPython.display import display, Markdown

'''    
+ Numeramos los polos de 0 a n=3


    (0)----Ya--(1)---Yc--(2)
                |         |
                Yb        G
                |         |
    (3)---------+----------
    
'''    

Ya, Yb, Yc = sp.symbols('Ya Yb Yc', complex=True)
G = sp.symbols('G', real=True, positive=True)

# Armo la MAI

#               Nodos: 0      1        2        3


Ymai = sp.Matrix([  
                    [ Ya,     -Ya,        0,     0 ],
                    [ -Ya,  Ya+Yb+Yc,   -Yc,    -Yb],
                    [ 0,         -Yc,  Yc+G,     -G],
                    [ 0,         -Yb,    -G,   Yb+G]
                 ])
# con_detalles = False
con_detalles = True

# Calculo la Z en el puerto de entrada a partir de la MAI

display(Markdown('### Calculo la impedancia de entrada a partir de la MAI' ))
Zmai = calc_MAI_impedance_ij(Ymai, 0, 3, verbose=con_detalles)

display(Markdown('### Verifico la transferencia de tension hallada en papel:' ))

Vmai = calc_MAI_vtransf_ij_mn(Ymai, 2, 3, 0, 3, verbose=con_detalles)  # Entrada en 0-3, salida en 2-3

Vmai = sp.symp