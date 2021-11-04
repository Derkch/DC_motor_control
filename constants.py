# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:14:31 2021

@author: alexd
"""

import numpy as np

J = 0.01
b = 0.1
K = 0.01
R = 1
L = 0.5

K_feedback = np.array([[0.0071, 0.4167]]) #Feedback gain matrix, calculated using LQR
