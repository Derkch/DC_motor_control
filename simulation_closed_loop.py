# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:58:46 2021

@author: alexd
"""

"""DC Motor simulation en lazo cerrado"""

from model_DC_motor import model_speed
from model_DC_motor import model_current

from regulator import regulator 

import matplotlib.pyplot as plt
import numpy as np

import init_conditions as ci

def main():
    
    #Simulacion:
    t_sim = 10.0 # s
    t_sample = 0.01 # s
    
    
    """Clock signal"""
    t = np.linspace(0.0, t_sim, int(t_sim/t_sample)+1)
    
    """Input signal"""
    ref = np.linspace(ci.D_THETA_REF, ci.D_THETA_REF, int(t_sim/t_sample)+1)
    
    """Output signals"""
    V = [ci.V_INI]
    
    d_theta = [ci.D_THETA_INI]
    i_l = [ci.I_L_INI]
    
    """Simulation loop"""
    
    for i in range(len(t)-1):
        
        """Control action"""
        V.append(regulator(ref[i], d_theta[i], i_l[i]))
        
        """Speed and current"""
        d_theta.append(model_speed(t[i], d_theta[0], d_theta[i], i_l[i]))
        i_l.append(model_current(t[i], i_l[0], i_l[i], V[i], d_theta[i]))
        
    
    fig, ax = plt.subplots()
    ax.plot(t, ref, label='Reference [rad/s]')
    ax.plot(t, d_theta, label='Output speed [rad/s]')
    plt.xlabel('Time (s)')
    plt.ylabel('Speed (rad/s)')
    #plt.ylim([0.0,4000.0])
    #plt.xlim([40.0, 100.0])
    legend = ax.legend(loc='lower center')
    plt.show()
    
    plt.figure()
    plt.plot(t, V, label= 'Voltage [V]')
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (V)')
    plt.show()
    

if __name__ == '__main__':
    
    main()