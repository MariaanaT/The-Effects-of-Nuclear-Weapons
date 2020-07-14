#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 21:23:13 2019

@author: mariaana
"""

# fig 9.16 
# page 392
# Dependence of fose rate from early fallout upon time after explosion

# X: time after explosion (hours)
# Y: Dose Rate (rads/hr)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('fig_9.16_p392.txt', sep=",", header = None)  

x_data = data.loc[:,0]
y_data = data.loc[:,1]

#https://stackoverflow.com/questions/18760903/fit-a-curve-using-matplotlib-on-loglog-scale 

# log(y) is some polynomial function of log(x), lets find the polynomial
logx = np.log(x_data)
logy = np.log(y_data)

degr = 7
# run numpy.polyfit on the logarithms of the data set
fit = np.polyfit(logx,logy,deg=degr, full=True)
#residual: 
residual = fit[1]
# deg = 2 -> residual =  5.10598  <- underfitting 
# deg = 3 -> residual =  1.9153   <- underfitting
# deg = 4 -> residual =  1.86826  <- underfitting
# deg = 5 -> residual =  1.44211  <- underfitting 
# deg = 6 -> residual =  0.934308 <- OK 
# deg = 7 -> residual =  0.683999 <- overfitting 

#coeffs: Polynomial coefficients, highest power first
coeffs = fit[0]
# 3:  
# 2:   
# 1:  
# 0:  
# y = exp( )

# poly: polynomial in log(x) that returns log(y)
poly = np.poly1d(coeffs)

# Get the fit to predict y values: define a function that exponentiates polynomial
yfit = lambda x: np.exp(poly(np.log(x)))
# predict with original data
y_pred = yfit(x_data)

# Mean squared error
error = np.mean((y_pred - y_data) ** 2)

# plot difference between original & predicted data 
plt.figure()
plt.scatter(y_data, y_pred-y_data)
#plt.xscale('log')
#plt.yscale('log')
plt.title('deg: %i,  MSE: %3.7f' % (degr, error))
plt.grid(b=True, color='black', linestyle='-')
plt.xlabel('Time')
plt.ylabel('Error btw prediction and data')
plt.show()

x_fit = np.logspace(-1,5.4,num=50,base=10)
# Get the fit to predict y values: define a function that exponentiates polynomial
yfit = lambda x: np.exp(poly(np.log(x)))
y_fit = yfit(x_fit) 

t_ref = x_fit**(-1.2)

#plot fitted line and original data on loglog plot
#plt.loglog(x_data, yfit(x_data))
fig = plt.figure()
ax = plt.gca()
plt.plot(x_fit, y_fit, color = 'blue', label = 'Fit to data points')
plt.plot(x_fit, t_ref, color = 'red', label ='t^-1.2 as reference')
plt.scatter(x_data, y_data, color = 'purple', label = 'Data points from original picture')
plt.yscale('log')
plt.xscale('log')
plt.axis([0.1, 250000, 0.00000001, 10])
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='gray', linestyle=':')
plt.title('Dependence of fose rate from early fallout upon time after explosion')
plt.xlabel('DTime after explosion (hr)')
plt.ylabel('Dose rate (rads/hr)')
ax.legend()
plt.show()
#fig.savefig('the name of your figure') 

"""
a =  1.0874402154591702E+02
b = -2.7431635070485289E-03
c =  4.6741861749216441E+03
d = -1.4912652559218996E-02

x = np.logspace(2,4.5,num=50,base=10,dtype='int')
print (x)

y = a * np.exp(b*x) + c * np.exp(d*x)
print(y)


pyplot.plot(x, y, color='blue', lw=2)
pyplot.plot(x_data, y_data, color = 'red')
pyplot.yscale('log')
pyplot.xscale('log')
pyplot.show()
"""
