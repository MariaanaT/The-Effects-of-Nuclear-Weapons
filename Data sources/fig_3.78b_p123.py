#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 23:21:42 2019

@author: mariaana
"""
# The effects of Nuclear Weapons 
# fig 3.78b, page 123
# https://www.fourmilab.ch/bombcalc/
# Reflected overpressure ratio for various side-on overpressures  
# at angle 0 deg, i.e., at normal incidence 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read in data 
data = pd.read_csv('fig_3.78b_p123.txt', sep=",", header = None)  

x_data = data.loc[:,1] #1: incident overpressure
y_data = data.loc[:,0] #0: reflected overpressure ratio


# run numpy.polyfit on the data set
degr = 3 
fit = np.polyfit(x_data, y_data, deg=degr, full=True)
#residual: 
residual = fit[1]
# deg = 2 -> residual = 0.0538922  <- underfitting 
# deg = 3 -> residual = 0.0032022  <- OK
# deg = 4 -> residual = 0.0031807  <- OK 
# deg = 5 -> residual = 0.0030661  <- overfitting 
# deg = 6 -> residual = 0.0015366  <- overfitting 

#coeffs: Polynomial coefficients, highest power first
coeffs = fit[0]
# 3:  5.81211e-07
# 2: -0.00027224
# 1:  0.050972
# 0:  2.04542

# poly: polynomial in log(x) that returns log(y)
poly = np.poly1d(coeffs)

# predict with original data
y_pred = poly(x_data)

# Mean squared error
error = np.mean((y_pred - y_data) ** 2)

# plot difference between original & predicted data 
plt.figure()
plt.scatter(y_data, y_pred-y_data)
plt.title('deg: %i,  MSE: %3.7f' % (degr, error))
plt.xlabel('Reflected overpressure ratio')
plt.ylabel('Error btw prediction and data')
plt.show() 

#predic values for plot
x_fit = np.linspace(0,200,num=101)
x_fit = x_fit.reshape(-1,1)
#x_trans = poly.fit_transform(x_fit)
#y_fit = regressor.predict(x_trans) 
y_fit = poly(x_fit) 

#plot fitted line and original data 
fig = plt.figure()
ax = plt.gca()
plt.plot(x_fit, y_fit, color = 'blue', label = 'Fit to data points')
plt.scatter(x_data, y_data, color = 'purple', label = 'Data points from original picture')
plt.axis([1, 200, 0, 6.5])
plt.xscale('log')
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='gray', linestyle=':')
plt.title(' Reflected overpressure ratio for various side-on overpressures\n\
           at normal incidence')
plt.xlabel('Incident overpressure (psi)')
plt.ylabel('Reflected overpressure ratio')
ax.legend()
plt.show()
#fig.savefig('the name of your figure') 
