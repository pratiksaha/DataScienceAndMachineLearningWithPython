#!/usr/bin/env python

import time
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import sklearn.metrics as skm

np.random.seed(int(time.time()))
pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds
plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

#split data to train and test set
trainX = pageSpeeds[:80]
trainY = purchaseAmount[:80]
trainx = np.array(trainX)
trainy = np.array(trainY)
plt.scatter(trainX, trainY)
plt.show()

testX = pageSpeeds[80:]
testY = purchaseAmount[80:]
testx = np.array(testX)
testy = np.array(testY)
plt.scatter(testX, testY)
plt.show()

poly_coeff = np.polyfit(trainx, trainy, 8) #fit a 8th degree polynomial
print "Polynomial Coefficients for 8th order", poly_coeff
poly_eqn = np.poly1d(poly_coeff)
print "Polynomial Equation of 8th degree"
print poly_eqn
nos = np.linspace(0, 7, 100) #generate 100 nos evenly spaced between 0 and 7

train_r2 = skm.r2_score(trainy, poly_eqn(trainx)) #Coefficient of Determination
print "R^2 for train data", train_r2
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(trainx, trainy)
plt.plot(nos, poly_eqn(nos), c='r')
plt.show()

test_r2 = skm.r2_score(testy, poly_eqn(testx)) #Coefficient of Determination
print "R^2 for train data", test_r2
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0, 200])
plt.scatter(testx, testy)
plt.plot(nos, poly_eqn(nos), c='r')
plt.show()
