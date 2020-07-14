# fig 3.72 
# page 109
# Peak overpressure from a 1-kiloton free air burst for sea-level ambient conditions

# X: Distance from burst (feet)
# Y: Peak overpressure (psi)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('fig_3.72_p109.txt', sep=",", header = None)  

x_data = data.loc[:,0]
y_data = data.loc[:,1]

#https://stackoverflow.com/questions/18760903/fit-a-curve-using-matplotlib-on-loglog-scale 

# log(y) is some polynomial function of log(x), lets find the polynomial
logx = np.log(x_data)
logy = np.log(y_data)

# run numpy.polyfit on the logarithms of the data set
fit = np.polyfit(logx,logy,deg=3, full=True)
#residual: 
residual = fit[1]
# deg = 2 -> residual = 0.0538315  <- underfitting 
# deg = 3 -> residual = 0.0102555  <- OK
# deg = 4 -> residual = 0.0102532  <- OK 
# deg = 5 -> residual = 0.00641033 <- overfitting 
# deg = 6 -> residual = 0.00220934 <- overfitting 

#coeffs: Polynomial coefficients, highest power first
coeffs = fit[0]
# 3: -0.0239369 
# 2:  0.720737 
# 1: -8.33536 
# 0: 33.1298 
# y = exp( )

# poly: polynomial in log(x) that returns log(y)
poly = np.poly1d(coeffs)

x_fit = np.logspace(2,4.5,num=50,base=10,dtype='int')
# Get the fit to predict y values: define a function that exponentiates polynomial
yfit = lambda x: np.exp(poly(np.log(x)))
y_fit = yfit(x_fit) 

#plot fitted line and original data on loglog plot
#plt.loglog(x_data, yfit(x_data))
fig = plt.figure()
ax = plt.gca()
plt.plot(x_fit, y_fit, color = 'blue', label = 'Fit to data points')
plt.scatter(x_data, y_data, color = 'purple', label = 'Data points from original picture')
plt.yscale('log')
plt.xscale('log')
plt.axis([100, 30000, 0.1, 2000])
plt.grid(b=True, which='major', color='black', linestyle='-')
plt.grid(b=True, which='minor', color='gray', linestyle=':')
plt.title('Peak overpressure from a 1 kiloton free air burst \n for sea level ambient conditions.')
plt.xlabel('Distance from burst (feet)')
plt.ylabel('Peak overpressure (psi)')
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
