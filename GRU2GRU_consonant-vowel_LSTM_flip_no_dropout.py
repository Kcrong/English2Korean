"""
Sequence to Sequence model

-- Inputs
Korean consonant, vowel   (ㄱ,ㄴ,ㄷ,ㄹ, ... ㅏ,ㅔ,ㅣ,ㅗ, ...)

자음, 모음을 출력하고 조합

Use LSTM at encoder
Flip the input of model

--- Without DROPOUT ---

"""

from os.path import splitext
file_name = splitext(__file__)[0]
print("Running: ", file_name)


## Disable debugging logs
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


## Ready for data Pre-Processing
space = [' ']

# Prepare English Data
big = [chr(i) for i in range(ord('A'), ord('Z')+1)]
small = [chr(i) for i in range(ord('a'), ord('z')+1)]

english_letter_list = big + small + space

idx2english = dict(enumerate(english_letter_list, 1))
english2idx = {v:k  for k,v in idx2english.items()}


# Prepare Korean Data
consonants = [chr(letter) for letter in range(ord('ㄱ'), ord('ㅎ')+1)]
vowel = [chr(letter) for letter in range(ord('ㅏ'), ord('ㅣ')+1)]

korean_letter_list = consonants + vowel + space

# Make a mapping with index
idx2korean = dict(enumerate(korean_letter_list, 1))
korean2idx = {v: k for k, v in idx2korean.items()}


## Read CSV file
import pandas as pd

df = pd.read_csv('data/full_data.csv', encoding='utf8')


## Load X
import numpy as np

roma = df['roma'].apply(lambda x: np.array([english2idx[letter] for letter in x]))
roma_df = pd.DataFrame(roma)
X = pd.DataFrame(roma_df['roma'].tolist()).values

# Replace nan to 0
X[np.isnan(X)] = 0

# Flip the input!!
X = np.flip(X, axis=1)


## Pre-processing func for y
from utils import Separater, sep_all

def sep_encode_all(sent):
    return [korean2idx[let] for letter in sent if letter != ' ' for let in Separater(letter).sep_all]

def encode_all(sep_sent):
    return [korean2idx[let] for let in sep_sent]

assert encode_all(sep_all('안녕 하세요')) == sep_encode_all('안녕 하세요')

# Load y
hang = df['hang'].apply(lambda x: sep_encode_all(x))
hang_df = pd.DataFrame(hang)
y = pd.DataFrame(hang_df['hang'].tolist()).values

# Replace nan to 0
y[np.isnan(y)] = 0

# One-hot Encoding
from keras.utils import np_utils
num_classes = len(korean_letter_list) + 1
y = np_utils.to_categorical(y, num_classes=num_classes).reshape(y.shape[0], y.shape[1], num_classes)


## Split train & test & validation set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.3)



## Hyper Parameters

from keras.layers import recurrent

# Parameters for the model and dataset
HIDDEN_SIZE = 200
BATCH_SIZE = 100
LAYERS = 2
MAX_EPOCHS = 1000
EMBEDDING_OUTPUT_SIZE = 200

encoder_RNN = recurrent.LSTM
decoder_RNN = recurrent.GRU
stop_monitor = 'val_acc'
stop_delta = 0.0
stop_epochs = 20


# ## Build Model

from keras.models import Sequential, load_model
from keras.layers import Dense, TimeDistributed, Activation, RepeatVector, Embedding


print('Build Model...')

model = Sequential()

model.add(Embedding(
    input_dim=len(english_letter_list)+1,  # 단어 갯수 + padding (1)
    output_dim=EMBEDDING_OUTPUT_SIZE,  # 출력 벡터
    input_length=X.shape[1]  # 입력 길이
))

model.add(encoder_RNN(HIDDEN_SIZE, return_sequences=True, input_shape=(X.shape[1], )))
model.add(encoder_RNN(HIDDEN_SIZE))

model.add(RepeatVector(y.shape[1]))  # Maximum output length

for _ in range(LAYERS):
    model.add(decoder_RNN(HIDDEN_SIZE, return_sequences=True))

model.add(TimeDistributed(Dense(len(korean_letter_list)+1)))
model.add(Activation('softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)


model.summary()
print('Done')


# Callbacks
from keras.callbacks import EarlyStopping, TensorBoard, ModelCheckpoint

## Visualize keras training status
from keras_tqdm import TQDMCallback

log_dir = './logs/' + file_name

callbacks_list = [
    EarlyStopping(
        monitor=stop_monitor,
        min_delta=stop_delta,
        patience=stop_epochs,
        verbose=1,
        mode='auto',
    ),
    TQDMCallback(
        leave_inner=False,
        leave_outer=True
    ),
    TensorBoard(
        log_dir=log_dir
    ),
    ModelCheckpoint(
        filepath='./models/' + file_name + '_checkpoint',
        monitor=stop_monitor,
        save_best_only=True,
        verbose=1,
        mode='auto',
    ),
]

hist = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    batch_size=BATCH_SIZE,
    epochs=MAX_EPOCHS,
    callbacks=callbacks_list,
    verbose=0
)

## Visualize history

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

plt.title(file_name)

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'g', label='val loss')
acc_ax.plot(hist.history['acc'], 'b', label='train acc')
acc_ax.plot(hist.history['val_acc'], 'r', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

image_path = 'results/' + file_name + '.png'
fig.savefig(image_path)
print()
print('Save graph at: ', image_path)


loss, acc = model.evaluate(X_test, y_test)

model.save('./models/' + file_name + '_latest')
print()
print("Save model at: ", './models/' + file_name + '_latest')

loaded_model = load_model('./models/' + file_name + '_checkpoint')
loaded_loss, loaded_acc = loaded_model.evaluate(X_test, y_test)

print()
print("Last Model: ")
print('Loss: %.2f' % loss)
print('Accuracy: %.2f' % acc)

print("Saved Best Model: ")
print('Loss: %.2f' % loaded_loss)
print('Accuracy: %.2f' % loaded_acc)