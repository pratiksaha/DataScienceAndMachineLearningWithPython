#!/usr/bin/env python

import numpy
import pandas
import pydot
import matplotlib.image
import matplotlib.pyplot
import sklearn.tree
import sklearn.externals.six
import sklearn.ensemble

df = pandas.read_csv("./data/PastHires.csv", header = 0)
print df.head()

d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)
print df.head()

features = list(df.columns[:6])
print "Features :", features

y = df["Hired"]
x = df[features]
clf = sklearn.tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

print "Decision Tree"
dot_data = sklearn.externals.six.StringIO()  
sklearn.tree.export_graphviz(clf, out_file=dot_data, feature_names=features)  
graph = pydot.graph_from_dot_data(dot_data.getvalue())  
png_str = graph.create_png(prog='dot')
sio = sklearn.externals.six.StringIO()
sio.write(png_str)
sio.seek(0)
img = matplotlib.pyplot.imread(sio)
imgplot = matplotlib.pyplot.imshow(img)
matplotlib.pyplot.show()

print "Ensemble Learning with Random Forest"
clf = sklearn.ensemble.RandomForestClassifier(n_estimators=10)
clf = clf.fit(x, y)
print clf.predict([[10, 1, 4, 0, 0, 0]])
print clf.predict([[10, 0, 4, 0, 0, 0]])
