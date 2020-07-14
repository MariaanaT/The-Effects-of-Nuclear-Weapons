#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:00:02 2019

@author: mariaana

Positive phase duration on the ground of overpressure 
and dynamic pressure for 1 kt burst  

"""

# fig 3.76
# page 119
# Positive phase duration on the ground of overpressure 
# and dynamic pressure for 1 kt burst  

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynom
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pylab 

# read in data 
data = pd.read_csv('fig_3.76_p119.txt', sep=",", header = None)  


# distance & height  
x_data = data.loc[:, 0:1] 
x_data.columns = ['d', 'h'] #distance & height

# time
y_data = data.loc[:, 2]
y_data.to_frame(name='t') # time

# transform data to polynomial form: 1, x, y, x^2, xy, y^2 ... 
degr = 4 # degree of polynomial 
poly = PolynomialFeatures(degr)
x_trans = poly.fit_transform(x_data)

# fit linear regression model to transformed data
regressor = LinearRegression()
regressor.fit(x_trans, y_data)

# predict with original data
y_pred = regressor.predict(x_trans) 

# Mean squared error
error = np.mean((y_pred - y_data) ** 2)
# deg = 2: 0.00021306732992967857
# deg = 3: 0.00011013885998653349
# deg = 4: 6.270733925791022e-05 <- OK
# deg = 5: 2.3813596437764135e-05

# plot difference between original & predicted data 
plt.figure()
plt.scatter(y_data, y_pred-y_data)
plt.title('deg: %i,  MSE: %3.7f' % (degr, error))
plt.xlabel('Time')
plt.ylabel('Error btw prediction and data')
plt.show() 

# coefficients from regression model  
coeff = regressor.coef_
intercept = regressor.intercept_

#poly.get_feature_names(x_data.columns)
#0:  1:          0.01654871784935602 # intercept 
#1:  d:          0.000264719
#2:  h:         -0.00024261
#3:  d^2:       -3.91739e-08
#4:  d h:        9.12183e-08
#5:  h^2:        7.34711e-07
#6:  d^3:        9.18797e-13
#7:  d^2 h:     -2.64512e-11
#8:  d h^2:     -4.95173e-10
#9:  h^3:       -2.71761e-10
#10: d^4:       -1.06355e-15
#11: d^3 h:      1.46488e-14
#12: d^2 h^2:    1.08149e-14
#13: d h^3:      2.35752e-13
#14: h^4:       -2.7244e-14

# create datapoints to cover the whole fig 
d_max = 3000 # distace range up to 6000 ft
h_max = 1200 # burst height up to 5000 ft
step = 50
d = np.arange(0, d_max+step, step) 
h = np.arange(0, h_max+step, step) 

# transform coefficients to matrix 
# powers as array
pwr = poly.powers_ 
# create and fill a coefficient matrix with the help of power indexes
coeff_mtrx = np.zeros(shape=(degr+1,degr+1))
for i in range(0, len(coeff)):
    coeff_mtrx[pwr[i][0]][pwr[i][1]] = coeff[i]
# add intercept     
coeff_mtrx[0][0] = intercept

# contourplot 
#https://www.python-course.eu/matplotlib_contour_plot.php
#https://matplotlib.org/users/colormaps.html
D, H = np.meshgrid(d, h) 
T = polynom.polyval2d(D, H, coeff_mtrx)    

# Image for late times 
levels_late = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4]
plt.figure()
pylab.xlim([0,d_max])
pylab.ylim([0,h_max])
contour = plt.contour(D, H, T, levels_late, colors = 'k') #contour lines 
plt.clabel(contour, colors = 'k', fmt = '%2.2f', fontsize=12) #contour labels
contour_filled = plt.contourf(D, H, T, levels_late, cmap=plt.cm.plasma) #filled
plt.colorbar(contour_filled) 
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='gray', linestyle=':')
plt.title('Positive phase duration (s) on the ground \nof overpressure, 1 kt burst')
plt.xlabel('Distance from ground zero (ft)')
plt.ylabel('Height of burst (ft)')
plt.show() 