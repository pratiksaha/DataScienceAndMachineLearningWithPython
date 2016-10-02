#!/usr/bin/env python

import numpy as np

listOfNumbers = [1, 2, 3, 4, 5, 6]
for number in listOfNumbers:
    print number,
    if (number % 2 == 0):
        print "is even"
    else:
        print "is odd"
print "All done."

A = np.random.normal(25.0, 5.0, 10)
print A

x = [1, 2, 3, 4, 5, 6]
print len(x)
print x
print x[:3]
print x[3:]
print x[-2:]
x.extend([7,8])
print x
x.append(9)
print x

y = [10, 11, 12]
listOfLists = [x, y]
print listOfLists
print y[1]

z = [3, 2, 1]
z.sort()
print z
z.sort(reverse=True)
print z

m = (1, 2, 3)
print len(m)
print m
n = (4, 5, 6)
print n[2]
listOfTuples = [m,n]
print listOfTuples
(age, income) = "32,120000".split(',')
print age
print income

captains = {}
captains["Enterprise"] = "Kirk"
captains["Enterprise D"] = "Picard"
captains["Deep Space Nine"] = "Sisko"
captains["Voyager"] = "Janeway"
print captains["Voyager"]
print captains.get("Enterprise")
print captains.get("NX-01")
for ship in captains:
    print ship + ": " + captains[ship]

def SquareIt(p):
    return p*p

print SquareIt(2)

def DoSomething(f, p):
    return f(p)

print DoSomething(SquareIt, 3)

print DoSomething(lambda p: p*p*p, 3)

print 1 == 3
print (True or False)
print 1 is 3
if 1 is 3:
    print "How did that happen?"
elif 1 > 3:
    print "Yikes"
else:
    print "All is well with the world"

for p in range(10):
    print p,
print ""
for p in range(10):
    if (p is 1):
        continue
    if (p > 5):
        break
    print p,
print ""
p = 0
while (p < 10):
    print p,
    p += 1
print ""
for p in range(100):
    if not p%2:
        print p,
print ""
