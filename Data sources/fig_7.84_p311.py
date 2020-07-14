#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 21:54:12 2019

@author: mariaana
"""

# The effects of Nuclear Weapons 
# fig 7.84, page 311
# https://www.fourmilab.ch/bombcalc/
# Fraction of thermal energy emitted vs normalized time in the thermal pulse 
# of an air burst below 100 000 feet

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read in data 
data = pd.read_csv('fig_7.84_p311.txt', sep=",", header = None)  

x_data = data.loc[:,0] # normalized time
y_data = data.loc[:,1] # normalized power 

# run numpy.polyfit on the data set
degr = 9
fit = np.polyfit(x_data, y_data, deg=degr, full=True)
#residual: 
residual = fit[1]
# deg = 2 -> residual = 0.0385467  <- underfitting 
# deg = 3 -> residual = 0.0123902  <- OK
# deg = 4 -> residual = 0.0123192  <- OK 
# deg = 5 -> residual = 0.00959547 <- overfitting 

#coeffs: Polynomial coefficients, highest power first
coeffs = fit[0]
# 3:  
# 2: 
# 1:  
# 0:  

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
plt.xlabel('Normalized power')
plt.ylabel('Error btw prediction and data')
plt.show() 

#predic values for plot
x_fit = np.linspace(0,10,num=101)
x_fit = x_fit.reshape(-1,1)
#x_trans = poly.fit_transform(x_fit)
#y_fit = regressor.predict(x_trans) 
y_fit = poly(x_fit) 

#plot fitted line and original data 
fig = plt.figure()
ax = plt.gca()
plt.plot(x_fit, y_fit, color = 'blue', label = 'Fit to data points')
plt.scatter(x_data, y_data, color = 'purple', label = 'Data points from original picture')
plt.axis([0, 10, 0, 1])
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='gray', linestyle=':')
plt.title(' Fraction of thermal energy emitted vs normalized time \n\
          in the thermal pulse of an air burst')
plt.xlabel('Normalized time')
plt.ylabel('Normalized power')
ax.legend()
plt.show()
#fig.savefig('the name of your figure') 
