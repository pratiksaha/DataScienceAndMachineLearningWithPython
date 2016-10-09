#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def reject_outliers(data):
    u = np.median(data)
    s = np.std(data)
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return filtered

print "\nSome Random Data:"
incomes = np.random.normal(27000, 15000, 10000)
print "Mean :", incomes.mean()
print "Std Dev :", incomes.std()
plt.hist(incomes,50)
plt.show()

print "\nAdded Some Outlier:"
incomes = np.append(incomes, [1000000000])
print "Mean :", incomes.mean()
print "Std Dev :", incomes.std()
plt.hist(incomes,50)
plt.show()

print "\nFiltered Data:"
incomes = reject_outliers(incomes)
print "Mean :", np.mean(incomes)
print "Std Dev :", np.std(incomes)
plt.hist(incomes, 50)
plt.show()
