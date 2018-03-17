import pandas as pd
import numpy as np
import random
np.set_printoptions(precision=3)

df = pd.read_csv('jester-data-1.csv')


# Label approx 10% of the dataset cells as 99, to denote they are part of the validation set.
# Keep the the actual values of the cells so you can use them later.

df_copy = df

print "start"

# Changes 10% of cells to 99
temp = 2498
for i in range(temp):
    x = random.randint(1, 100)

    if df_copy.iloc[i, x] != 99:
        # print "POS: ", i, x
        # print "OLD: ", df_copy.iloc[i, x]
        df_copy.iloc[i, x] = 99
        # print "NEW: ", df_copy.iloc[i, x]
        # print "\n"
    else:
        temp += 1

n_features = 5

user_ratings = df_copy.values
latent_user_preferences = np.random.random((user_ratings.shape[0], n_features))
latent_item_features = np.random.random((user_ratings.shape[1], n_features))

print "done 1"


def predict_rating(user_id, item_id):
    # Predict a rating given a user_id and an item_id.

    user_preference = latent_user_preferences[user_id]
    item_preference = latent_item_features[item_id]
    return user_preference.dot(item_preference)
print "done 2"


def train(user_id, item_id, rating, alpha = 0.0001):

    # print item_id
    prediction_rating = predict_rating(user_id, item_id)
    err = (prediction_rating - rating)
    # print err
    user_pref_values = latent_user_preferences[user_id][:]
    latent_user_preferences[user_id] -= alpha * \
        err * latent_item_features[item_id]
    latent_item_features[item_id] -= alpha * err * user_pref_values
    return err
print "done 3"

np.predict = []


# for i in range(len(df_copy)):
#     for j in range(len(df_copy.iloc[i])):
#         if df_copy.iloc[i,j] == 99:
#             np.predict.append(predict_rating(i,j))
#
# print "done 4"
#
# for i in range(len(df_copy)):
#     for j in range(len(df_copy.iloc[i])):
#         train(i, j, np.predict[j])
#
# print "done 5"


def sgd(iterations = 10):
    # Iterate over all users and all items and train for a certain number of iterations
    for iteration in range(0,iterations):
        error = []
        for user_id in range(0,latent_user_preferences.shape[0]):
            for item_id in range(0,latent_item_features.shape[0]):
                rating = user_ratings[user_id][item_id]
                if(not np.isnan(rating)):
                    err = train(user_id,item_id,rating)
                    error.append(err)
        mse = (np.array(error) ** 2).mean()
        if(iteration % 10000 == 0):
            print "MSE:", mse

print "Starting sgd()"
sgd()



# placeholder text
