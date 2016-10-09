#!/usr/bin/env python

import operator
import pandas
import numpy
import scipy.spatial

def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = scipy.spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance

def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors

print "Ratings :"
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pandas.read_csv('./data/movielens/u.data', sep='\t', names=r_cols, usecols=range(3))
print ratings.head()

print "\nGrouping by total and average ratings :"
movieProperties = ratings.groupby('movie_id').agg({'rating': [numpy.size, numpy.mean]})
print movieProperties.head()

print "\nNormalising..."
movieNumRatings = pandas.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - numpy.min(x)) / (numpy.max(x) - numpy.min(x)))
print movieNormalizedNumRatings.head()

print "\nGetting genre info.."
movieDict = {}
with open(r'/home/pratiksaha/Untitled Folder/ml-100k/u.item') as f:
    temp = ''
    for line in f:
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])      
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, genres, movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))
print "Sample Data ", movieDict[1]
print "Sample Data ", movieDict[2]
print "Sample Data ", movieDict[3]
print "Sample Data ", movieDict[4]
print "\nDistance b/w movie %s & %s is %s\n" %(movieDict[2][0], movieDict[4][0], ComputeDistance(movieDict[2], movieDict[4]))
K = 10
avgRating = 0
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print movieDict[neighbor][0] + " " + str(movieDict[neighbor][3])
    avgRating /= float(K)
print "\nAvg rating for %s nearest neighbours to %s is %s\n" %(K, movieDict[1][0], avgRating)
