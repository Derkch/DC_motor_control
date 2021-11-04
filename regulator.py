# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:00:05 2021

@author: alexd
"""

import init_conditions as ci
import constants as cte
import state_space_model as ss
import numpy as np

def regulator(reference_point: float, d_theta: float, i: float) -> float:
    
    y_ref = reference_point
    
    x = np.array([[d_theta],
                  [i]])
    r = np.matmul(ss.M_inv, np.array([[0.0],
                                      [0.0],
                                      [y_ref]]))
    x_ref = r[0:2]
    u_ref = float(r[2])
    
    u = float(np.matmul(cte.K_feedback, x_ref - x)) + u_ref
    return u