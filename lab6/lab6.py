import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# num of rows in df
n = 50000
s = 2

print "Start \n"

df = pd.read_csv("hUSCensus1990raw50K.csv")


df_demo = pd.DataFrame()


df_demo["AGE"] = df[["AGE"]].copy()
df_demo["INCOME"] = df[["INCOME" + str(i) for i in range(1, 8)]].sum(axis=1)
df_demo["YEARSCH"] = df[["YEARSCH"]].copy()
df_demo["ENGLISH"] = df[["ENGLISH"]].copy()
df_demo["FERTIL"] = df[["FERTIL"]].copy()
df_demo["YRSSERV"] = df[["YRSSERV"]].copy()


g = sns.pairplot(df_demo, vars=["AGE", "INCOME"])
print "pairplot done \n"

g.savefig("output.png")
print "fig saved \n"


df_demo = pd.get_dummies(df_demo, columns=["ENGLISH", "FERTIL"])

X = df_demo.values[np.random.choice(df_demo.values.shape[0], 10000)]

from sklearn import metrics
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_db = sc.fit_transform(X)


n_clusters = 0
coeffs = []
coeffs2 = []

for n_clusters in range(2, 11):
    labels = KMeans(n_clusters=n_clusters).fit_predict(X_db)
    labels2 = AgglomerativeClustering(n_clusters = n_clusters).fit_predict(X_db)
    print "\n"
    print('Number of clusters: %d' % n_clusters)

    print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X_db, labels))

    x = (metrics.silhouette_score(X_db, labels))
    x2 = (metrics.silhouette_score(X_db, labels2))

    coeffs.append([x])
    coeffs2.append([x2])

    # print "Coeffs: ", coeffs
    # print "Coeffs2: ", coeffs2


min_coeff = min(coeffs)

print "Min Silhouette Coefficient is: ", min_coeff


for i in range(10):
    skip = sorted(np.random.choice(range(1, n), n - s - 1, replace=False))
    s += 1
    df_copy = pd.read_csv("hUSCensus1990raw50K.csv", skiprows = skip)


data_output = []
data_output2 = []

for i in range(0, 8):
    for j in range(1):
        data_output.append(coeffs[i][j])
        data_output2.append(coeffs2[i][j])


sns_plot1 = sns.pointplot(data=[data_output])
sns_plot2 = sns.pointplot(data=[data_output2])

fig1 = sns_plot1.get_figure()
fig1.savefig("kmeans.png")

fig2 = sns_plot2.get_figure()
fig2.savefig("agglo.png")



print data_output
print data_output2

print "fin \n"















# end code
