import pandas as pd
import numpy as np
import random
np.set_printoptions(precision = 3)

df = pd.read_csv('jester-data-1.csv')



# Label approx 10% of the dataset cells as 99, to denote they are part of the validation set.
# Keep the the actual values of the cells so you can use them later.

df_copy = df

count = 0


# get 99 count
for i in range(len(df_copy)):
    for j in range(len(df_copy[i])):
        if df_copy[i,j] == 99:
            count = count + 1
    print count


# Changes 10% of cells to 99
# for i in range(2498):
    # x = random.randint(1,100)
    # print "POS: ", i, x
    # print "OLD: ", df_copy.iloc[i,x]
    # df_copy.iloc[i,x] = 99
    # print "NEW: ", df_copy.iloc[i,x]
    # print "\n"
