#!/usr/bin/env python

import os
import io
import numpy as np
import pandas as pd
import sklearn.feature_extraction as skf
import sklearn.naive_bayes as skn

def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                 if inBody:
                     lines.append(line)
                 elif line == '\n':
                     inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message

def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)
    return pd.DataFrame(rows, index=index)

print "Loading data..."
data = pd.DataFrame({'message': [], 'class': []})
data = data.append(dataFrameFromDirectory('./data/emails/spam', 'spam'))
data = data.append(dataFrameFromDirectory('./data/emails/ham', 'ham'))
print data.head()

vectorizer = skf.text.CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)
targets = data['class'].values

print "Performing Naive Bayes Classification..."
classifier = skn.MultinomialNB()
classifier.fit(counts, targets)

print "Predicting..."
examples = ['Free Viagra now!!!', "Hi Bob, how about a game of golf tomorrow?"]
example_counts = vectorizer.transform(examples)
predictions = classifier.predict(example_counts)

print examples
print predictions
