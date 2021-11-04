# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:21:49 2021

@author: alexd
"""

import constantes as cte
import numpy as np

a11 = float(-cte.b/cte.J)
a12 = float(cte.K/cte.J)
a21 = float(-cte.K/cte.L)
a22 = float(-cte.R/cte.L)

b11 = float(0.0)
b21 = float(1/cte.L)

c11 = float(1.0)
c12 = float(0.0)

d11 = float(0.0)

""" M = [A B
         C 0]

Esta matriz se usa para el calculo del estado de referencia y la accion de control
de referencia.
"""
M_inv = np.linalg.inv(np.array([[a11, a12, b11],
                                [a21, a22, b21],
                                [c11, c12, 0.0]]))
#M_inv = np.linalg.inv(M)