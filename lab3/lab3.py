import numpy as np
import csv
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score as acc
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer


df = pd.read_csv('bank-additional-full.csv', delimiter = ";")

# Creates copy of df
df_copy = df




# Convert to dummies
df_dummies = pd.get_dummies(df)
# Deletes columns "y_no" and "duration"
del df_dummies["y_no"]
del df_dummies["duration"]
# print df_dummies

# Generates histogram for y_yes
x_ax = df_dummies["y_yes"]
plot = sns.distplot(x_ax, kde = False, rug = False)
plot.figure.savefig("y_yes_Histo.png")

train_dummies = df_dummies
del train_dummies["y_yes"]

print df_dummies
print train_dummies

X = df_dummies
y = train_dummies


X, y = make_classification(n_samples=100, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)

clf = RandomForestClassifier(max_depth=2, random_state=0)

clf.fit(X, y)
print clf.feature_importances_
print clf.predict([[0, 0, 0, 0]])

scores = cross_val_score(clf, X, y, cv=10,scoring = make_scorer(acc))
print "Scores: ", scores
