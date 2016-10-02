#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

vals = np.random.normal(10, 0.5, 10000)

print "50th Percentile :", np.percentile(vals, 50)
print "90th Percentile :", np.percentile(vals, 90) 
print "20th Percentile :", np.percentile(vals, 20)
print "Mean :", np.mean(vals)
print "Variance :", np.var(vals)
print "Skewness :", sp.skew(vals)
print "Kurtosis :", sp.kurtosis(vals)

print "Median :", np.median(vals)
print "Mode :", sp.mode(vals)
print "Arithmetic mean :", sp.tmean(vals)
print "Geometric mean :", sp.gmean(vals)
print "Harmonic mean :", sp.hmean(vals)
for i in range(10):
    print i, "th moment", sp.moment(vals, moment=i)

plt.hist(vals, 50)
plt.show()
