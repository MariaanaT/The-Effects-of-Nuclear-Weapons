#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:38:23 2019

@author: mariaana

Given distance and height from the blast wave for a given yield (kt), calculate
 - duration (t) and
 - arrival time (t)
of the blast wave

"""
import numpy as np

"""

posit_phase_duration

# Positive phase duration on the ground of overpressure for 1 kt burst 
 
d = Distance from burst (ft)
h = Burst height (ft)
t_d = positive pahase duration (s)

If no height is given, presuming surface burst. 

Can be applied to distances up to 3000 ft and heights up to 1200 ft. 

Source: The Effects of Nuclear Weapons 
 fig 3.76, page 119

"""

def posit_phase_duration(d, h = 0): 
    
    A = 0.0165487178    #0:  1 intercept 
    B = 0.000264719     #1:  d
    C = -0.00024261     #2:  h
    D = -3.91739e-08    #3:  d^2
    E = 9.12183e-08     #4:  d h 
    F = 7.34711e-07     #5:  h^2 
    G = 9.18797e-13     #6:  d^3 
    H = -2.64512e-11    #7:  d^2 h
    I = -4.95173e-10    #8:  d h^2 
    J = -2.71761e-10    #9:  h^3 
    K = -1.06355e-15    #10: d^4 
    L = 1.46488e-14     #11: d^3 h  
    M = 1.08149e-14     #12: d^2 h^2 
    N = 2.35752e-13     #13: d h^3  
    O = -2.7244e-14     #14: h^4 

    if (d > 0.0) & (d < 3000.0) & (h >= 0.0) & (h < 1200.0): 
        t_d = (  A        + B * d        + C * h 
               + D * d**2 + E * d * h    + F * h**2 
               + G * d**3 + H * d**2 * h + I * d * h**2    + J * h**3 
               + K * d**4 + L * d**3 * h + M * d**2 * h**2 + N * d * h**3 + O * h**4 )
    else:  
        print('To calculate positive phase duration\n\
distance must be less than 3000 ft,\n\
and burst height less than 1200 ft.\n') 
        t_d = np.NaN
    
    return t_d

"""
arrival_time

# Arrival time on the ground of blast wave for 1 kt burst 
 
d = Distance from burst (ft)
h = Burst height (ft)
t_a = Arrival time (s)

If no height is given, presuming surface burst. 

Source: The Effects of Nuclear Weapons 
 fig 3.77, page 121

"""

def arrival_time(d, h = 0): 
    
    A = -0.0757263486   #0:  1 intercept 
    B =  0.000242327    #1:  d
    C =  0.000229512    #2:  h
    D =  2.9119e-07     #3:  d^2
    E = -1.0623e-07     #4:  d h 
    F =  3.603e-07      #5:  h^2 
    G = -5.38702e-11    #6:  d^3 
    H = -6.19025e-12    #7:  d^2 h
    I = -1.89457e-11    #8:  d h^2 
    J = -8.22902e-11    #9:  h^3 
    K =  3.34121e-15    #10: d^4 
    L =  3.43878e-15    #11: d^3 h  
    M = -2.31707e-15    #12: d^2 h^2 
    N =  5.48898e-15    #13: d h^3  
    O =  6.66132e-15    #14: h^4 

    if (d > 0.0) & (d < 6000.0) & (h >= 0.0) & (h < 5000.0): 
        t_a = (  A        + B * d        + C * h 
               + D * d**2 + E * d * h    + F * h**2 
               + G * d**3 + H * d**2 * h + I * d * h**2    + J * h**3 
               + K * d**4 + L * d**3 * h + M * d**2 * h**2 + N * d * h**3 + O * h**4 )
    else:  
        print('To calculate arrival time \n\
distance must be less than 6000 ft,\n\
and burst height less than 5000 ft.\n') 
        t_a = np.NaN
        
    return t_a


"""
MAIN

"""

print('\nGive distance (ft), height (ft) and yield (kt) of burst to calculate\n \
 - positive phase duration (s) on the ground of overpressure\n \
 - Arrival time (s) on the ground of blast wave ')

d = float(input('Distance from burst (ft): '))
h = float(input('Height of burst (ft): '))
W = float(input('Energy yield of explosion (kt): '))

# scaled distance for 1 kt explosion (cubic root) 
d_scaled = d / np.cbrt(W)
h_scaled = h / np.cbrt(W)
 
t_d = posit_phase_duration(d_scaled, h_scaled)
t_a = arrival_time(d_scaled, h_scaled)

t_d_scaled = t_d * np.cbrt(W)
t_a_scaled = t_a * np.cbrt(W)

print('\nPositive phase duration:\n %6.3f s' % t_d_scaled)
print('Arrival_time:\n %6.3f s'% t_a_scaled)
    

    