#!/usr/bin/env python

import itertools
import matplotlib.pyplot
import sklearn.datasets
import sklearn.decomposition
import sklearn.svm
import sklearn.cross_validation

print "Iris Data..."
iris = sklearn.datasets.load_iris()
print iris.data
numSamples, numFeatures = iris.data.shape
print "Samples :", numSamples
print "Features :", numFeatures
print "Target Names :", list(iris.target_names)

print "\n2D data with normalisation..."
pca_2d = sklearn.decomposition.PCA(n_components=2, whiten=True).fit(iris.data)
data_2d = pca_2d.transform(iris.data)
print data_2d

print "\n1D data with normalisation..."
pca_1d = sklearn.decomposition.PCA(n_components=1, whiten=True).fit(iris.data)
data_1d = pca_1d.transform(iris.data)
print data_1d

print "\n2D PCA :"
print "\nEigen Vectors :"
print pca_2d.components_
print "\nInformation (variance) preserved :"
print pca_2d.explained_variance_ratio_
print "\nTotal Variance preserved :"
print sum(pca_2d.explained_variance_ratio_)

colors = itertools.cycle('rgb')
target_ids = range(len(iris.target_names))
matplotlib.pyplot.figure()
for i, c, label in zip(target_ids, colors, iris.target_names):
    matplotlib.pyplot.scatter(data_2d[iris.target == i, 0], data_2d[iris.target == i, 1], c=c, label=label)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

print "\n1D PCA :"
print "\nEigen Vectors :"
print pca_1d.components_
print "\nInformation (variance) preserved :"
print pca_1d.explained_variance_ratio_
print "\nTotal Variance preserved :"
print sum(pca_1d.explained_variance_ratio_)

print "\nK fold cross validation with 60% training and 40% testing :\n"
X_train, X_test, y_train, y_test = sklearn.cross_validation.train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

print "Running SVC with default(i.e degree=3) poly kernel on training data"
clf = sklearn.svm.SVC(kernel='poly').fit(X_train, y_train)
print "Score with training data:", clf.score(X_train, y_train)
print "Score with test data:", clf.score(X_test, y_test)
print "Using cross validation Scores :"
scores = sklearn.cross_validation.cross_val_score(clf, iris.data, iris.target, cv=5)
print scores
print "Mean Score : %s \n" %(scores.mean())

print "Running SVC with poly kernel of degree 2 on training data"
clf = sklearn.svm.SVC(kernel='poly', degree=2).fit(X_train, y_train)
print "Score with training data:", clf.score(X_train, y_train)
print "Score with test data:", clf.score(X_test, y_test)
print "Using cross validation Scores :"
scores = sklearn.cross_validation.cross_val_score(clf, iris.data, iris.target, cv=5)
print scores
print "Mean Score : %s \n" %(scores.mean())

print "Running SVC with linear kernel on training data"
clf = sklearn.svm.SVC(kernel='linear').fit(X_train, y_train)
print "Score with training data:", clf.score(X_train, y_train)
print "Score with test data:", clf.score(X_test, y_test)
print "Using cross validation Scores :"
scores = sklearn.cross_validation.cross_val_score(clf, iris.data, iris.target, cv=5)
print scores
print "Mean Score : %s \n" %(scores.mean())
