import numpy as np
import csv
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

# This will read in the files, remove and NaN values, and plot as scatter and histograms
file1 = r'Current_Fleet.csv'
file2 = r'New_Fleet.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

df1 = df1.dropna(axis=0, how='any')
df2 = df2.dropna(axis=0, how='any')

# df1.plot(kind = 'scatter', x = "Number", y = "Current Fleet")
# df2.plot(kind = 'scatter', x = "Number", y = "New Fleet")
# df1.plot(kind = 'hist', x = 'Number', y = "Current Fleet")
# df2.plot(kind = 'hist', x = 'Number', y = "New Fleet")


data1 = df1.values.T[1]
data2 = df2.values.T[1]

sns_plot = sns.distplot(df1, bins = 20, kde = False, rug = True).get_figure()
sns_plot2 = sns.distplot(df2, bins = 20, kde = False, rug = True).get_figure()



show = raw_input("Would you like to save plots? ")

if show == 'yes' or show == 'y':
    sns_plot.savefig("scaterplot_currentFleet.png", bbox_inches='tight')
    sns_plot2.savefig("scaterplot_newFleet.png", bbox_inches='tight')
elif show != 'yes' or show != 'y':
    print "OK"

print "Current Fleet STD"
print np.std(data1), "\n"

print "Current Fleet STD"
print np.std(data2), "\n"
