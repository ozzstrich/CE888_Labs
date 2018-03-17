import matplotlib
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


print "\n Standard Deviation:"
# Reads in files and seperates coloumn data while removing all NaN values from col2
df = pd.read_csv('./vehicles.csv')
currentFleet_data = df.values.T[0]
proposedFleet_data = df.dropna().values.T[1]



def bootstrap(statistic_func, iterations, data):
    samples = np.random.choice(data,replace = True, size = [iterations, len(data)])
    # print samples.shape
    data_mean = data.mean()
    vals = []
    for sample in samples:
        sta = statistic_func(sample)
        # print sta
        vals.append(sta)
    b = np.array(vals)
    # print b
    lower, upper = np.percentile(b, [2.5, 97.5])
    return data_mean,lower, upper


samples = 100
boot = bootstrap(np.std, samples, currentFleet_data)
print "STD for Current Fleet: ", np.std(currentFleet_data)
print("STD Lower Bound : %f" % boot[1])
print("STD Upper Bound: %f" % boot[2])

print "\n"

boot = bootstrap(np.std, samples, proposedFleet_data)
print "STD for Proposed Fleet: ", np.std(proposedFleet_data)
print("STD Lower Bound : %f" % boot[1])
print("STD Upper Bound: %f" % boot[2])


# # PLOTS
# # Scatter
# sns_plot = sns.lmplot(df.columns[0], df.columns[1], data = df, fit_reg = False)
# sns_plot.axes[0,0].set_ylim(0,)
# sns_plot.axes[0,0].set_xlim(0,)
# sns_plot.savefig("vehicles_scatter.png", bbox_inches = "tight")

# # Histograms
# plt.clf()
# axes = plt.gca()
# sns_plot2 = sns.distplot(currentFleet_data, bins = 20, kde = False, rug = True).get_figure()
# sns_plot2.savefig("current_histogram.png", bbox_inches = "tight")
#
# plt.clf()
# axes = plt.gca()
# sns_plot2 = sns.distplot(proposedFleet_data, bins = 20, kde = False, rug = True).get_figure()
# sns_plot2.savefig("proposed_histogram.png", bbox_inches = "tight")
#















































    # end code
