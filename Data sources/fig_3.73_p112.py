#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:20:32 2019

@author: mariaana
"""

# The effects of Nuclear Weapons 
# fig 3.73a-c, page 111-115
# https://www.fourmilab.ch/bombcalc/
# Peak overpressures on the ground for a 1-kt burst 
# as a function of burst height 
# Optimum height of burst for the given overpressure

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read in data 
data = pd.read_csv('fig_3.73_p112.txt', sep=",", header = None)  

#0: distance
#1: height
#2: overpressure

"""
Optimal height vs peak overpressure
"""

x_data = data.loc[:,1] #1: height
y_data = data.loc[:,2] #2: overpressure 

# log(y) is some polynomial function of log(x), lets find the polynomial
logx = np.log(x_data)
logy = np.log(y_data)

degr = 5
# run numpy.polyfit on the logarithms of the data set
fit = np.polyfit(logx,logy,deg=degr, full=True)
#residual: 
residual = fit[1]
# deg = 2 -> residual =  <- underfitting 
# deg = 3 -> residual =   <- underfitting
# deg = 4 -> residual =   <- underfitting 
# deg = 5 -> residual =    <- OK 
# deg = 6 -> residual =   <- underfitting 

#coeffs: Polynomial coefficients, highest power first
coeffs = fit[0]
# 5:    0.0600126
# 4:   -1.6741
# 3:   18.1864
# 2:  -95.9073
# 1:  242.448
# 0: -223.567
# y = exp( )

# poly: polynomial in log(x) that returns log(y)
poly = np.poly1d(coeffs)

# Get the fit to predict y values: define a function that exponentiates polynomial
yfit = lambda x: np.exp(poly(np.log(x)))
# predict with original data
y_pred = yfit(x_data)
#y_pr_log = np.log(y_pred)

# Mean squared error
#error = np.mean((y_pred - logy) ** 2)
error = np.mean((y_pred - y_data) ** 2)

# plot difference between original & predicted data 
plt.figure()
#plt.scatter(logy, y_pred-logy)
plt.scatter(y_data, y_pred-y_data)
plt.xscale('log')
#plt.yscale('log')
plt.title('deg: %i,  MSE: %3.7f' % (degr, error))
plt.grid(b=True, color='black', linestyle='-')
plt.xlabel('Peak overpressure')
plt.ylabel('Error btw prediction and data')
plt.show()

#predict for plot 
x_fit = np.logspace(1,4,num=100,base=10, endpoint=True)
y_fit = yfit(x_fit) 

#plot fitted line and original data on loglog plot
#plt.loglog(x_data, yfit(x_data))
fig = plt.figure()
ax = plt.gca()
plt.plot(x_fit, y_fit, color = 'blue', label = 'Fit to data points')
plt.scatter(x_data, y_data, color = 'purple', label = 'Data points from original picture')
plt.xscale('log')
plt.yscale('log')
plt.axis([50, 2000, 1, 10000])
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='gray', linestyle=':')
plt.title('Peak overpressure from a 1 kiloton free air burst \n for sea level ambient conditions.')
plt.xlabel('Optimal Burst height (feet)')
plt.ylabel('Peak overpressure (psi)')
ax.legend()
plt.show()
#fig.savefig('the name of your figure') 

"""
Optimal height vs distance
""" 
x_data = data.loc[:,0] #0: distance 
y_data = data.loc[:,1] #1: height

# log(y) is some polynomial function of log(x), lets find the polynomial
logx = np.log(x_data)
logy = np.log(y_data)

degr = 4
# run numpy.polyfit on the logarithms of the data set
fit = np.polyfit(logx,logy,deg=degr, full=True)
#residual: 
residual = fit[1]
# deg = 2 -> residual = 0.282647 <- underfitting 
# deg = 3 -> residual = 0.249331 <- underfitting
# deg = 4 -> residual = 0.134491 <- OK 
# deg = 5 -> residual = 0.133064 <- OK 
# deg = 6 -> residual = 0.124597 <- overfitting 

#coeffs: Polynomial coefficients, highest power first
coeffs = fit[0]
# 4:   0.0329679
# 3:  -0.882183
# 2:   8.56463
# 1: -34.8477
# 0:  54.2089
# y = exp( )

# poly: polynomial in log(x) that returns log(y)
poly = np.poly1d(coeffs)

# Get the fit to predict y values: define a function that exponentiates polynomial
yfit = lambda x: np.exp(poly(np.log(x)))
# predict with original data
y_pred = yfit(x_data)
#y_pr_log = np.log(y_pred)

# Mean squared error
#error = np.mean((y_pred - logy) ** 2)
error = np.mean((y_pred - y_data) ** 2)

# plot difference between original & predicted data 
plt.figure()
#plt.scatter(logy, y_pred-logy)
plt.scatter(y_data, y_pred-y_data)
plt.xscale('log')
#plt.yscale('log')
plt.title('deg: %i,  MSE: %3.7f' % (degr, error))
plt.grid(b=True, color='black', linestyle='-')
plt.xlabel('Burst height')
plt.ylabel('Error btw prediction and data')
plt.show()

#predict for plot 
x_fit = np.logspace(1.7,4.1,num=100,base=10, endpoint=True)
y_fit = yfit(x_fit) 

#plot fitted line and original data on loglog plot
#plt.loglog(x_data, yfit(x_data))
fig = plt.figure()
ax = plt.gca()
plt.plot(x_fit, y_fit, color = 'blue', label = 'Fit to data points')
plt.scatter(x_data, y_data, color = 'purple', label = 'Data points from original picture')
plt.xscale('log')
plt.yscale('log')
plt.axis([50, 7000, 50, 2000])
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='gray', linestyle=':')
plt.title('Optimal burst height for a 1 kiloton free air burst \n for sea level ambient conditions.')
plt.xlabel('Distance (feet)')
plt.ylabel('Optimal Burst height (feet)')
ax.legend()
plt.show()
#fig.savefig('the name of your figure') 

