#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:46:41 2019

@author: mariaana

Arrival time of the blast wave for 1 kt burst 
"""

# fig 3.77 
# page 121
# Arrival times on the ground of blast wave for 1 kt burst 

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as polynom
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pylab 

# https://stackabuse.com/linear-regression-in-python-with-scikit-learn/
# https://stats.stackexchange.com/questions/58739/polynomial-regression-using-scikit-learn

# read in data 
data = pd.read_csv('fig_3.77_p121.txt', sep=",", header = None)  

# distance & height  
x_data = data.loc[:, 0:1] 
x_data.columns = ['d', 'h'] #distance & height

# time
y_data = data.loc[:, 2]
y_data.to_frame(name='t') # time

# transform data to polynomial form: 1, x, y, x^2, xy, y^2 ... 
degr = 4
poly = PolynomialFeatures(degr)
x_trans = poly.fit_transform(x_data)

# fit linear regression model to transformed data
regressor = LinearRegression()
regressor.fit(x_trans, y_data)

# predict with original data
y_pred = regressor.predict(x_trans) 

# Mean squared error
error = np.mean((y_pred - y_data) ** 2)
#deg = 2: 0.003696879
#deg = 3: 0.001188880
#deg = 4: 0.000348032 <- OK 
#deg = 5: 0.000102702

# plot difference between original & predicted data 
plt.figure()
plt.scatter(y_data, y_pred-y_data)
plt.title('deg: %i,  MSE: %3.5f' % (degr, error))
plt.xlabel('Time')
plt.ylabel('Error btw prediction and data')
plt.show() 

# coefficients from regression model  
coeff = regressor.coef_
intercept = regressor.intercept_

#poly.get_feature_names(x_data.columns)
#0:  1:        0.00000000e+00
#1:  d:        2.42326594e-04,  
#2:  h:        2.29512430e-04,  
#3:  d^2:      2.91189726e-07,
#4:  d h:     -1.06230212e-07,  
#5:  h^2:      3.60299733e-07, 
#6:  d^3:     -5.38702066e-11, 
#7:  d^2 h:   -6.19024773e-12,
#8:  d h^2:   -1.89456839e-11, 
#9:  h^3:     -8.22901724e-11,  
#10: d^4:      3.34121294e-15,  
#11: d^3 h:    3.43877758e-15,
#12: d^2 h^2: -2.31706879e-15,  
#13: d h^3:    5.48897679e-15,  
#14: h^4:      6.66132460e-15
   
# create datapoints to cover the whole fig 
d_max = 6000 # distace range up to 6000 ft
h_max = 5000 # burst height up to 5000 ft
step = 100
d = np.arange(0, d_max+step, step) 
h = np.arange(0, h_max+step, step) 
"""
# predict the whole Fig 3.77 
x_tmp = []
for i,j in itertools.product(d, h):
    x_tmp.extend([[i, j]])
x_test = pd.DataFrame(x_tmp)
# transform datapoints to polynomial form
x_test_tr = poly.fit_transform(x_test)
# time predictions for the whole fig 
y_test = regressor.predict(x_test_tr)
"""
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
D, H = np.meshgrid(d, h) 
#T = x_test
#T['y'] = y_test
#T = (intercept           + coeff[1]*D**1*H**0  + coeff[2]*D**0*H**1 
#   + coeff[3]*D**2*H**0  + coeff[4]*D**1*H**1  + coeff[5]*D**0*H**2 
#   + coeff[6]*D**3*H**0  + coeff[7]*D**2*H**1  + coeff[8]*D**1*H**2  + coeff[9]*D**0*H**3
#   + coeff[10]*D**4*H**0 + coeff[11]*D**3*H**1 + coeff[12]*D**2*H**2 + coeff[13]*D**1*H**3 + coeff[14]*D**0*H**4 )
T = polynom.polyval2d(D, H, coeff_mtrx)    

# Image for late times 
levels_late = [0.2,0.4, 0.6, 0.8, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6]
plt.figure()
pylab.xlim([0,d_max])
pylab.ylim([0,h_max])
contour = plt.contour(D, H, T, levels_late, colors = 'k') #contour lines 
plt.clabel(contour, colors = 'k', fmt = '%2.1f', fontsize=12) #contour labels
contour_filled = plt.contourf(D, H, T, levels_late) #filled
plt.colorbar(contour_filled) 
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.title('Late arrival times (s)')
plt.xlabel('Distance (ft)')
plt.ylabel('Height (ft)')
plt.show()

# Image for early times 
levels_early = [0.04, 0.07, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7,0.8]
plt.figure()
pylab.xlim([0,1300])
pylab.ylim([0,1000])
contour = plt.contour(D, H, T, levels_early, colors = 'k') #contour lines 
plt.clabel(contour, colors = 'k', fmt = '%2.2f', fontsize=12) #contour labels
contour_filled = plt.contourf(D, H, T, levels_early) #filled
plt.colorbar(contour_filled) 
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.title('Early arrival times (s)')
plt.xlabel('Distance (ft)')
plt.ylabel('Height (ft)')
plt.show()
