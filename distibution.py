#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

print "Uniform distribution"
values = np.random.uniform(-10.0, 10.0, 100000)
plt.hist(values, 50)
plt.show()

print "Normal distribution"
x = np.arange(-3, 3, 0.001)
plt.plot(x, sp.norm.pdf(x))
plt.show()

print "Normal distribution wth given mu and sigma"
mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values, 50)
plt.show()

print "Exponential distribution"
x = np.arange(0, 10, 0.001)
plt.plot(x, sp.expon.pdf(x))
plt.show()

print "Binomial distribution"
n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x, sp.binom.pmf(x, n, p))
plt.show()

print "Poisson distribution"
mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, sp.poisson.pmf(x, mu))
plt.show()
