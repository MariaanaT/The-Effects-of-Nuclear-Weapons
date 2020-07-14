#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:08:46 2019

@author: mariaana

Given distance from surface burst (ft), calculate 
- maximum overpressure (psi)
- maximum dynamic pressure (psi)
- maximum velocity (ft/s)

"""
import numpy as np

"""
max_overpressure 

Peak overpressure from a 1 kiloton free air burst
 for sea level ambient conditions.
 
x = Distance from burst (feet)
p = Peak overpressure (psi)

Source: The Effects of Nuclear Weapons 
 fig 3.72, page 109

"""

def max_overpressure(x): 
    
    a = -0.0239369 # 3
    b =  0.720737  # 2
    c = -8.33536   # 1
    d = 33.1298    # 0

    p = np.exp(a*np.log(x)**3 + b*np.log(x)**2 + c*np.log(x) + d)
    return p

"""
# testing by printing
plt.plot(x, y)
plt.yscale('log')
plt.xscale('log')
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='gray', linestyle=':')
plt.show()
"""

"""
max_dynamic_pressure

Dynamic pressure as a function of peak (max) overpressure 
at sea level ambient conditions 

q:     dynamic pressure (psi)
p:     peak overpressure (psi)
P_0:   ambient pressure (psi)
       at sea level P_0 =14.70 psi 
gamma: ratio of specific heats 
       for air gamma = 1.4 at moderate temperatures

Source: The Effects of Nuclear Weapons 
 eq. 3.55.1, page 97
 see also fig 3.55, pg 98
"""

def max_dynamic_pressure(p): 

    gamma = 1.4
    P_0 = 14.70     
    q = p**2 / (2 * gamma * P_0 + (gamma - 1)*p)
    return q 

"""
max_velocity

Particle velocity or peak wind velocity behind the shock front
as a function of peak (max) overpressure 
at sea level ambient conditions 

u:     particle velocity, or peak wind velocity (ft/s)
p:     peak overpressure (psi)
c_0:   speed of sound (ft/s)
       in air at sea level c_0 = 1116 ft/sec
P_0:   ambient pressure (psi)
       at sea level P_0 =14.70 psi 
gamma: ratio of specific heats 
       for air gamma = 1.4 at moderate temperatures

Source: The Effects of Nuclear Weapons 
 in the beginning of the right column at page 97
 see also fig 3.55, pg 98
"""

def max_velocity(p): 

    c_0 = 1116 
    gamma = 1.4
    P_0 = 14.70     
    
    u = c_0 * p / (gamma * P_0) * np.sqrt((1 + (gamma + 1) / (2 * gamma) * p / P_0 )**-1)
    
    return u

"""
Refl_overpressure

Reflected overpressure ratio for various side-on overpressures  
at angle 0 deg, i.e., at normal incidence 

r = Reflected overpressure (-)
p = Incident overpressure (psi)

Source: The Effects of Nuclear Weapons 
  fig 3.78b, page 123
https://www.fourmilab.ch/bombcalc/

"""

def refl_overpressure(p): 
    
    a =  5.81211e-07 # 3
    b = -0.00027224  # 2
    c =  0.050972    # 1
    d =  2.04542     # 0

    if (p > 1) & (p < 201): 
        r = p * (a*p**3 + b*p**2 + c*p + d)
    else :
        print('To calculate reflected overpressure \n\
              incident overpressure must be less than 200 psi.\n') 
        r = np.NaN
    return r

"""
opt_burst_height 

Optimal burst height for a 1 kt burst in a standard sea-level atmosphere

x = distance from burst (ft)
h = optimal burst height (ft)

Source: The Effects of Nuclear Weapons 
 fig 3.73a-c, page 111-115
https://www.fourmilab.ch/bombcalc/

"""

def opt_burst_height(x):  
    
    a =   0.0329679  # 4
    b =  -0.882183   # 3
    c =   8.56463    # 2
    d = -34.8477     # 1
    e =  54.2089     # 0

    x_min = 50
    x_max = 7000
   
    if (x > x_min) & (x < x_max): 
        h = np.exp(a*np.log(x)**4 + b*np.log(x)**3 + c*np.log(x)**2 + d*np.log(x) + e)
    else :
        print('To calculate optimal burst height \n\
              distance must be less than %6.1f ft' % x_max) 
        h = np.NaN
    return h

"""
max_pressure_opt_height 

Peak overpressure (psi) from optimal burst height 
as a function of distance from ground zero (ft)

x = distance from burst (ft)
p = peak overpressure (psi)

Source: The Effects of Nuclear Weapons 
 fig 3.73a-c, page 111-115
https://www.fourmilab.ch/bombcalc/

"""

def max_pressure_opt_height(x):  
    
    a =    0.0600126 # 5
    b =   -1.6741    # 4
    c =   18.1864    # 3
    d =  -95.9073    # 2
    e =  242.448     # 1
    f = -223.567     # 0

    x_min = 50
    x_max = 7001
   
    if (x > x_min) & (x < x_max): 
        h = np.exp(a*np.log(x)**5 + b*np.log(x)**4 + c*np.log(x)**3 + d*np.log(x)**2 + e*np.log(x) + f)
    else :
        print('To calculate peak overpressure of optimal burst height, \n\
              distance must be less than %6.1f ft' % x_max) 
        h = np.NaN
    return h


"""
MAIN

"""

print('Give distance (ft) and yield (kt) of burst to calculate \n\
      - maximum overpressure (psi) \n\
      - maximum dynamic pressure (psi) \n\
      - maximum velocity (ft/s) \n\
      of surface burst and burst at optimal burst height.')
x = float(input('Distance from burst (ft): '))
W = float(input('Energy yield of explosion (kt): '))
# scaled distance for 1 kt explosion (cubic root) 
x_scaled = x / np.cbrt(W)

if (x > 50.0) & (x < 30000.0): 
    p_s = max_overpressure(x_scaled)
    q_s = max_dynamic_pressure(p_s)
    u_s = max_velocity(p_s)
    
    h = opt_burst_height(x_scaled)
    p_h = max_pressure_opt_height(h)
    q_h = max_dynamic_pressure(p_h)
    u_h = max_velocity(p_h)

    print('\nSurface burst:')
    print(' - Maximum overpressure:\n %6.3f psi' % p_s)
    print(' - Maximum dynamic pressure:\n %6.3f psi'% q_s)
    print(' - Maximum velocity:\n %6.3f ft/s' % u_s)
    
    print('\nBurst at optimal height:')
    print(' - Optimal height:\n %6.3f ft' % h)
    print(' - Maximum overpressure:\n %6.3f psi' % p_h)
    print(' - Maximum dynamic pressure:\n %6.3f psi'% q_h)
    print(' - Maximum velocity:\n %6.3f ft/s' % u_h)
    
else:  
    print('Distance must be 200 - 30000 ft.') 
   