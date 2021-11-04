# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:10:49 2021

@author: alexd
"""

"""DC Motor simulation en lazo abierto"""

from model_DC_motor import model_speed
from model_DC_motor import model_current

import matplotlib.pyplot as plt
import numpy as np

import init_conditions as ci

def main():
    
    #Simulacion:
    t_sim = 10.0 # s
    t_sample = 0.01 # s
    
    
    """Clock signal"""
    t = np.linspace(0.0, t_sim, int(t_sim/t_sample)+1)
    
    """"Input signal"""
    
    V = np.linspace(ci.V_INI, ci.V_INI, int(t_sim/t_sample)+1)
    
    """Output signals"""
    d_theta = [ci.D_THETA_INI]
    i_l = [ci.I_L_INI]
    
    """Simulation loop"""
    
    for i in range(len(t)-1):
        
        d_theta.append(model_speed(t[i], d_theta[0], d_theta[i], i_l[i]))
        i_l.append(model_current(t[i], i_l[0], i_l[i], V[i], d_theta[i]))
        
    plt.figure()
    plt.plot(t, d_theta, label='d_theta [rad/s]')
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Speed (rad/s)')
    plt.show()

if __name__ == '__main__':
    
    main()