#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def reject_outliers(data):
    u = np.median(data)
    s = np.std(data)
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return filtered

#random data
incomes = np.random.normal(27000, 15000, 10000)
print incomes.mean()
print incomes.std()
plt.hist(incomes,50)
plt.show()

#add some outlier
incomes = np.append(incomes, [1000000000])
print incomes.mean()
print incomes.std()
plt.hist(incomes,50)
plt.show()

#filter outliers
filtered = reject_outliers(incomes)
print np.mean(filtered)
print np.std(filtered)
plt.hist(filtered, 50)
plt.show()

