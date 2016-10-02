#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def de_mean(x):
    xmean = np.mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n-1)

def correlation(x, y):
    stddevx = np.std(x)
    stddevy = np.std(y)
    return covariance(x,y) / stddevx / stddevy

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmountBogus = 100 - pageSpeeds * 3
purchaseAmount = np.random.normal(50.0, 10.0, 1000)
purchaseAmountSpeed = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

print "Speed v/s Bogus Amount"
print "Covariance", covariance(pageSpeeds, purchaseAmountBogus)
print np.cov(pageSpeeds, purchaseAmountBogus)
print "Correlation", correlation(pageSpeeds, purchaseAmountBogus)
print np.corrcoef(pageSpeeds, purchaseAmountBogus)
plt.scatter(pageSpeeds, purchaseAmountBogus)
plt.show()

print "Speed v/s Amount"
print "Covariance", covariance(pageSpeeds, purchaseAmount)
print np.cov(pageSpeeds, purchaseAmount)
print "Correlation", correlation(pageSpeeds, purchaseAmount)
print np.corrcoef(pageSpeeds, purchaseAmount)
plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

print "Speed v/s Speed Amount"
print "Covariance", covariance(pageSpeeds, purchaseAmountSpeed)
print np.cov(pageSpeeds, purchaseAmountSpeed)
print "Correlation", correlation(pageSpeeds, purchaseAmountSpeed)
print np.corrcoef(pageSpeeds, purchaseAmountSpeed)
plt.scatter(pageSpeeds, purchaseAmountSpeed)
plt.show()
