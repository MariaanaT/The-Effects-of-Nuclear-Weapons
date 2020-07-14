#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 23:21:42 2019

@author: mariaana
"""

# fig 3.78b
# page 123
# Reflected overpressure ratio as a function of angle of incidence
# for various side-on overpressures   

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# read in data 
data = pd.read_csv('fig_3.78b_p123.txt', sep=",", header = None)  

data.columns = ['a', 'r', 'p']

# handle only one pverpressure value at a time
overpressure = 50
data_a = data.loc[data['p'] == overpressure]

# angle & 
#x_data = data.loc[:, 0:1] 
x_data = data_a[['a']]

# reflected overpressure ratio 
y_data = data_a.loc[:, 'r']
y_data.to_frame(name='r') # ratio

# transform data to polynomial form: 1, x, y, x^2, xy, y^2 ... 
degr = 3 # degree of polynomial 
poly = PolynomialFeatures(degr)
x_trans = poly.fit_transform(x_data)

# fit linear regression model to transformed data
regressor = LinearRegression()
regressor.fit(x_trans, y_data)

# predict with original data
y_pred = regressor.predict(x_trans) 

# Mean squared error
error = np.mean((y_pred - y_data) ** 2)
# deg = 2: 
# deg = 3: 
# deg = 4: 
# deg = 5: 

# plot difference between original & predicted data 
plt.figure()
plt.scatter(y_data, y_pred-y_data)
plt.title('deg: %i,  MSE: %3.7f' % (degr, error))
plt.xlabel('overpressure')
plt.ylabel('Error btw prediction and data')
plt.show() 

# coefficients from regression model  
coeff = regressor.coef_
intercept = regressor.intercept_

#predic values for plot
x_fit = np.linspace(0,90,num=91)
x_fit = x_fit.reshape(-1,1)
x_trans = poly.fit_transform(x_fit)
y_fit = regressor.predict(x_trans) 

#poly.get_feature_names(x_data.columns)

# Image
#levels = [5, 10, 20, 50]
plt.figure()
#pylab.xlim([0,d_max])
#pylab.ylim([0,h_max])
plt.plot(x_fit, y_fit, color = 'blue', label = 'Fit to data points')
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='gray', linestyle=':')
plt.title('Reflected overpressure ratio as a function of angle of incidence\nfor various side-on overpressures')
plt.xlabel('Angle of incidence')
plt.ylabel('Reflected overpressure ratio')
plt.show() 