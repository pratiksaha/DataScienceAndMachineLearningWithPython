#!/usr/bin/env python

import sys
import time
import numpy
import matplotlib.pyplot
import sklearn.cluster
import sklearn.preprocessing
import sklearn.metrics

#build some clusters in data
def createClusteredData(N, k):
    numpy.random.seed(int(time.time()))
    pointsPerCluster = float(N)/k
    X = []
    for i in range (k):
        incomeCentroid = numpy.random.uniform(20000.0, 200000.0)
        ageCentroid = numpy.random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([numpy.random.normal(incomeCentroid, 10000.0), numpy.random.normal(ageCentroid, 2.0)])
    X = numpy.array(X)
    return X

data = createClusteredData(100, 5)

print "creating clusters"
model = sklearn.cluster.KMeans(n_clusters=5)
print "fitting data with scaling"
model = model.fit(sklearn.preprocessing.scale(data))
print "Model labels"
print model.labels_ 
print "Model cluster centers"
print model.cluster_centers_
print "Model inertia"
print model.inertia_
matplotlib.pyplot.figure(figsize=(8, 6))
matplotlib.pyplot.scatter(data[:,0], data[:,1], c=model.labels_.astype(numpy.float))
matplotlib.pyplot.show()

print "Finding best cluster based on silhouette_avg"
scaled_data = sklearn.preprocessing.scale(data)
best_cluster_no = 1
best_cluster_silhouette_avg = -1.0
cluster_dict = {}
for i in range(9):
    n_clusters = i+2
    print "creating %s clusters" %(n_clusters)
    model = sklearn.cluster.KMeans(n_clusters=n_clusters)
    print "fitting data with scaling"
    model = model.fit(scaled_data)
    print "labels :", model.labels_
    print "cluster centers :"
    print model.cluster_centers_
    print "inertia :", model.inertia_
    silhouette_avg = sklearn.metrics.silhouette_score(scaled_data, model.labels_)
    print "silhouette average :", silhouette_avg
    if (silhouette_avg > best_cluster_silhouette_avg):
        best_cluster_silhouette_avg = silhouette_avg
        best_cluster_no = n_clusters
    cluster_dict[n_clusters] = silhouette_avg
    matplotlib.pyplot.figure(figsize=(8, 6))
    matplotlib.pyplot.scatter(data[:,0], data[:,1], c=model.labels_.astype(numpy.float))
    matplotlib.pyplot.show()
    print ""

print "Best cluster is %s with silhouette_avg %s" %(best_cluster_no, best_cluster_silhouette_avg)
for key, value in cluster_dict.iteritems():
    print "%s => %s" %(key, value)
