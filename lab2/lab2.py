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


df1.plot(kind = 'scatter', x = 'Current Fleet', y = "Number")

df2.plot(kind = 'scatter', x = 'New Fleet', y = "Number")

df1.plot(kind = 'hist', x = 'Number', y = "Current Fleet")

df2.plot(kind = 'hist', x = 'Number', y = "New Fleet")

show = raw_input("Output scatter plot and histogram? ")

if show == 'yes' or show == 'y':
    plt.show()
elif show != 'yes' or show != 'y':
    print "OK"

print "Current Fleet STD"
print df1.std(), "\n"

print "Current Fleet STD"
print df2.std(), "\n"
