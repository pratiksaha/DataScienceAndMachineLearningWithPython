#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#generate some random income data
incomes = np.random.normal(27000, 15000, 10000)
print "For income data :"
print "Mean : ", incomes.mean()
print "Variance : ", incomes.var()
print "Standard Deviation : ", incomes.std()
print "Median : ", np.median(incomes)
plt.hist(incomes, 50)
plt.show()

#add an outlier
incomes = np.append(incomes, [1000000000])
print "Income data with outlier :"
print "Mean : ", np.mean(incomes)
print "Variance : ", np.var(incomes)
print "Standard Deviation : ", np.std(incomes)
print "Median : ", np.median(incomes)

#generate some random spending data
spendings = np.random.normal(100.0, 20.0, 10000)
print "For spending data :"
print "Mean : ", np.mean(spendings)
print "Variance : ", np.var(spendings)
print "Standard Deviation : ", np.std(spendings)
print "Median : ", np.median(spendings)
plt.hist(spendings, 50)
plt.show()

#generate some random queue data
queue = np.random.normal(10.0, 2.0, 10000)
print "For queue data :"
print "Mean : ", np.mean(queue)
print "Variance : ", np.var(queue)
print "Standard Deviation : ", np.std(queue)
print "Median : ", np.median(queue)
plt.hist(queue, 20)
plt.show()

#generate some random age data
ages = np.random.randint(low=18, high=90, size=500)
print "Age data :"
print ages
mode_result = stats.mode(ages)
print "Mode value is %s with %s occurences" %(mode_result.mode, mode_result.count)
plt.hist(ages, 100)
plt.show()
