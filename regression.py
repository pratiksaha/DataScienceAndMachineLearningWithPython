#!/usr/bin/env python

import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import sklearn.metrics as skm
import pandas as pd
import statsmodels.api as sm

np.random.seed(int(time.time()))
pageSpeeds = np.random.normal(3.0, 1.0, 1000)

print "Linear Regression"
purchaseAmountLinear = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3
plt.scatter(pageSpeeds, purchaseAmountLinear)
plt.show()
slope, intercept, r_value, p_value, std_err = sp.linregress(pageSpeeds, purchaseAmountLinear)
print "Slope", slope
print "Intercept", intercept
print "R value", r_value
print "P value", p_value
print "Std Err", std_err
print "R squared", r_value ** 2
fitLine = [ slope * x + intercept for x in pageSpeeds]
plt.scatter(pageSpeeds, purchaseAmountLinear)
plt.plot(pageSpeeds, fitLine, c='r')
plt.show()
print ""

print "Polynomial Regression"
purchaseAmountPolynomial = np.random.normal(50.0, 10.0, 1000) / pageSpeeds
plt.scatter(pageSpeeds, purchaseAmountPolynomial)
plt.show()
x = np.array(pageSpeeds)
y = np.array(purchaseAmountPolynomial)

poly_coeff = np.polyfit(x, y, 4) #fit a 4th degree polynomial
print "Polynomial Coefficients for 4th order", poly_coeff
poly_eqn = np.poly1d(poly_coeff)
print "Polynomial Equation of 4th order"
print poly_eqn
r2 = skm.r2_score(y, poly_eqn(x)) #Coefficient of Determination
print "R^2", r2
nos = np.linspace(0, 7, 100) #generate 100 nos evenly spaced between 0 and 7
plt.scatter(x, y)
plt.plot(nos, poly_eqn(nos), c='r')
plt.show()
print ""

degree_r2_dict = {}
best_deg = 0
best_r2 = 0.0
print "Fitting polynomials from degree 1 to 20\n" 
for i in range(20):
    deg = i+1
    print "Fitting a %s th degree polynomial" %(deg) 
    poly_coeff = np.polyfit(x, y, deg)
    print "Polynomial Coefficients for %s th degree :" %(deg), poly_coeff
    poly_eqn = np.poly1d(poly_coeff)
    print "Polynomial Equation of %s th degree :" %(deg)
    print poly_eqn
    r2 = skm.r2_score(y, poly_eqn(x))
    print "R^2 value for %s th degree polynomial is %s" %(deg, r2)
    if (r2 > best_r2):
        best_r2 = r2
        best_deg = deg
    degree_r2_dict[deg] = r2
    nos = np.linspace(0, 7, 100)
    plt.scatter(x, y)
    plt.plot(nos, poly_eqn(nos), c='r')
    plt.show()
    print ""
print "Best r^2 value is %s for degree %s" %(best_r2, best_deg)
print "Comparision for degree v/s r^2 :"
for key, value in degree_r2_dict.iteritems():
    print "%s => %s" %(key, value)
print ""

print "Multivariate Regression"
df = pd.read_excel("./data/cars.xls")
print df.head()
#Convert some data from Categorical data to Ordinal Data
df['Make_ord'] = pd.Categorical(df.Make).codes
df['Model_ord'] = pd.Categorical(df.Model).codes
df['Trim_ord'] = pd.Categorical(df.Trim).codes
df['Type_ord'] = pd.Categorical(df.Type).codes
print "Fitting Prices to Mileage, Model and Doors"
X = df[['Mileage', 'Model_ord', 'Doors']]
y = df[['Price']]
X1 = sm.add_constant(X)
est = sm.OLS(y, X1).fit() #fit using Ordinary Least Squares
print est.summary()
print y.groupby(df.Doors).mean()
print y.groupby(df.Make_ord).mean()
print y.groupby(df.Model_ord).mean()
print y.groupby(df.Trim_ord).mean()
print y.groupby(df.Type_ord).mean()
print "Fitting Prices to Mileage, Make, Model, Trim and Type"
X2 = df[['Mileage', 'Make_ord', 'Model_ord', 'Trim_ord', 'Type_ord']]
est = sm.OLS(y, X2).fit()
print est.summary()
