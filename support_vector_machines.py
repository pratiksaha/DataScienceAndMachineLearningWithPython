#!/usr/bin/env python

import sys
import time
import numpy
import matplotlib.pyplot
import sklearn.svm


#build some clusters in data
def createClusteredData(N, k):
    numpy.random.seed(int(time.time()))
    pointsPerCluster = float(N)/k
    X = []
    Y = []
    for i in range (k):
        incomeCentroid = numpy.random.uniform(20000.0, 200000.0)
        ageCentroid = numpy.random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([numpy.random.normal(incomeCentroid, 10000.0), numpy.random.normal(ageCentroid, 2.0)])
            Y.append(i)
    X = numpy.array(X)
    Y = numpy.array(Y)
    return X, Y

#plot the predictions
def plotPredictions(clf):
    xx, yy = numpy.meshgrid(numpy.arange(0, 250000, 10), numpy.arange(10, 70, 0.5))
    Z = clf.predict(numpy.c_[xx.ravel(), yy.ravel()])
    matplotlib.pyplot.figure(figsize=(8, 6))
    Z = Z.reshape(xx.shape)
    matplotlib.pyplot.contourf(xx, yy, Z, cmap=matplotlib.pyplot.cm.Paired, alpha=0.8)
    matplotlib.pyplot.scatter(X[:,0], X[:,1], c=Y.astype(numpy.float))
    matplotlib.pyplot.show()
                                    

#run C-Support Vector Classification with a kernel
def runSVC(X, Y, kernel='rbf'):
    print "Running SVC with %s kernel..." %(kernel)
    svc = sklearn.svm.SVC(kernel=kernel).fit(X, Y)
    plotPredictions(svc)
    print svc.predict([[200000, 40]])
    print svc.predict([[50000, 65]])
    print "Score :", svc.score(X,Y)


print "Input Data..."
(X, Y) = createClusteredData(100, 5)
matplotlib.pyplot.figure(figsize=(8, 6))
matplotlib.pyplot.scatter(X[:,0], X[:,1], c=Y.astype(numpy.float))
matplotlib.pyplot.show()

runSVC(X, Y)
runSVC(X, Y, 'linear')
runSVC(X, Y, 'poly')
runSVC(X, Y, 'sigmoid')
runSVC(X, Y, 'precomputed')
