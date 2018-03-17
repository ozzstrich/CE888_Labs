import numpy as np
import csv
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns


file = r'vehicles.csv'
df = pd.read_csv(file)

# # Removes NaN
# df = df.dropna(axis=0, how='any')

# Get Current Fleet Data
currentFleet = df.iloc[:, 0]
currentFleet = currentFleet.values.T
print currentFleet
currentFleetY = len(currentFleet)
print "Current Fleet count: ", currentFleetY

# Get New Fleet Data
newFleet = df.iloc[:, 1]
newFleet = newFleet.dropna(axis = 0, how = 'any')
newFleet = newFleet.values.T
print newFleet
newFleetY = len(newFleet)
print "New Fleet count: ",newFleetY


def returnCount():
    for i in range(currentFleet):
        return i


sns_plot = sns.lmplot(currentFleet, returnCount(), data = currentFleet, fit_reg = False)
sns_plot.axes[0, 0].set_ylim(0,)
sns_plot.axes[0, 0].set_xlim(0,)
sns_plot.savefig("currentFleet.png", bbox_inches ='tight')


# Plot Scatter
# df.plot(kind = 'scatter', x = 'Current fleet', y = 'New Fleet')
# print(df)
# plt.show()

# Plot Histo
# df.plot(kind = 'hist', x = 'Current fleet', y = 'New Fleet')
# print(df)
# plt.show()
