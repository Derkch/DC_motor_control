# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:10:49 2021

@author: alexd
"""

"""DC Motor simulation en lazo abierto"""

from modelo_motor_DC import modelo_velocidad
from modelo_motor_DC import modelo_corriente

import matplotlib.pyplot as plt
import numpy as np

import condiciones_iniciales as ci

def main():
    
    #Simulacion:
    t_sim = 10.0 # s
    t_sample = 0.01 # s
    
    
    """Senyal de reloj"""
    t = np.linspace(0.0, t_sim, int(t_sim/t_sample)+1)
    
    """Senyales de entrada"""
    
    V = np.linspace(ci.V_INI, ci.V_INI, int(t_sim/t_sample)+1)
    
    """Senyales de salida"""
    d_theta = [ci.D_THETA_INI]
    i_l = [ci.I_L_INI]
    
    """Bucle de simulacion"""
    
    for i in range(len(t)-1):
        
        d_theta.append(modelo_velocidad(t[i], d_theta[0], d_theta[i], i_l[i]))
        i_l.append(modelo_corriente(t[i], i_l[0], i_l[i], V[i], d_theta[i]))
        
    plt.figure()
    plt.plot(t, d_theta, label='n [rpm]')
    plt.legend()
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (rpm)')
    plt.show()

if __name__ == '__main__':
    
    main()