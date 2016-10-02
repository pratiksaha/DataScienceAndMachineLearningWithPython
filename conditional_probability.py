#!/usr/bin/env python

import time
import numpy

numpy.random.seed(int(time.time()))

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0
for _ in range(100000):
    ageDecade = numpy.random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = float(ageDecade) / 100.0
    totals[ageDecade] += 1
    if (numpy.random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1

print "Totals :", totals
print "Purchases :", purchases
print "Total Purchases :", totalPurchases

PEF = float(purchases[30]) / float(totals[30])
print "P(purchase | 30s) :", PEF

PF = float(totals[30]) / 100000.0
print "P(30's) :", PF

PE = float(totalPurchases) / 100000.0
print "P(Purchase) :", PE

print "P(30's)P(Purchase) :", PE * PF
print "P(30's, Purchase) :", float(purchases[30]) / 100000.0
print "P(purchase | 30s) :", (float(purchases[30]) / 100000.0) / PF
