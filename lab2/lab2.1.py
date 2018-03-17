import matplotlib
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Reads in files and seperates coloumn data while removing all NaN values from col2
df = pd.read_csv('./vehicles.csv')
currentFleet_data = df.values.T[0]
proposedFleet_data = df.dropna().values.T[1]

print "STD for Current Fleet: ", np.std(currentFleet_data)
print "STD for Proposed Fleet: ", np.std(proposedFleet_data)

# PLOTS

# Scatter
sns_plot = sns.lmplot(df.columns[0], df.columns[1], data = df, fit_reg = False)
sns_plot.axes[0,0].set_ylim(0,)
sns_plot.axes[0,0].set_xlim(0,)
sns_plot.savefig("vehicles_scatter.png", bbox_inches = "tight")

# Histograms
plt.clf()
axes = plt.gca()
sns_plot2 = sns.distplot(currentFleet_data, bins = 20, kde = False, rug = True).get_figure()
sns_plot2.savefig("current_histogram.png", bbox_inches = "tight")

plt.clf()
axes = plt.gca()
sns_plot2 = sns.distplot(proposedFleet_data, bins = 20, kde = False, rug = True).get_figure()
sns_plot2.savefig("proposed_histogram.png", bbox_inches = "tight")




















































    # end code
