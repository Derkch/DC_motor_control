# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:12:54 2021

@author: alexd
"""

import numpy as np
from scipy.integrate import odeint
import constants as cte


def dif_eq_acceleration(d_theta: np.ndarray, t: float, i: float, c = 0) -> float:
    
    return float((cte.K*i - cte.b*d_theta)/cte.J) #return acceleration (d_2_theta)

def dif_eq_current(i: np.ndarray, t: float, V: float, d_theta: float) -> float:
    
    return float((V - cte.K*d_theta - cte.R*i)/cte.L) #returns current variation (d_i)

def model_speed(t: np.ndarray, d_theta_0: float, d_theta: float, i: float) -> float:
    
    if t == 0.00:
        d_theta_ini = d_theta_0
        t = np.array([0.00, 0.01])
    else:
        d_theta_ini = d_theta
        t = np.array([t, t+0.01])
        
    return float(np.array(odeint(dif_eq_acceleration, d_theta_ini, t, args=(i, 0)))[1])


def model_current(t: np.ndarray, i_0: float, i: float, V: float, d_theta: float) -> float:
    
    if t == 0.00:
        i_ini = i_0
        t = np.array([0.00, 0.01])
    else:
        i_ini = i
        t = np.array([t, t+0.01])
        
    return float(np.array(odeint(dif_eq_current, i_ini, t, args=(V, d_theta)))[1])
    
 