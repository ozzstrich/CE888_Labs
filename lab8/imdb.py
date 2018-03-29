
from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.preprocessing import sequence
from keras.models import Model
from keras.layers import Dense, Activation, Embedding, Flatten, Input, LSTM, Dropout, Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb

max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

print('Loading data...')
(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=max_features)
print(len(X_train), 'train sequences')
print(len(X_test), 'test sequences')

print (X_train[0])

print('Pad sequences (samples x time)')
X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

print('Build model...')


inputs = Input(shape=(maxlen,))
x = inputs
x = Embedding(max_features, 128, dropout=0.2)(x)
# 1) Original scores (Test score: 0.6877648611035, Test accuracy: 0.83672)


# 2) 64 neuron relu layer (Test score: 1.11207178636, Test accuracy: 0.8206)
# x = Dense(64, activation = 'relu')(x)

# 3) Dropout Layer set to 20% (Test score: 1.25892501183, Test accuracy: 0.80784)
# x = Dropout(0.2)(x)

# 4) Remove 2 and 3, add conv layer followed by relu, and global max pooling (Test score: 0.975063895037 Test accuracy: 0.82568)
# x = Conv1D(64, kernel_size = (4), strides = (2), activation = 'relu')(x)
# x = GlobalMaxPooling1D()(x)

# 5) Add LSTM Layer instead of 4 (Test score: 0.975871128669, Test accuracy: 0.82764)
# x = LSTM(64, activation = 'relu')(x)


# x = Flatten()(x)
x = Dense(1)(x)
predictions = Activation("sigmoid")(x)

model = Model(input=inputs, output=predictions)
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=15,
          validation_data=(X_test, y_test))
score, acc = model.evaluate(X_test, y_test,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
