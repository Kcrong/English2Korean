"""
Sequence to Sequence model

-- Inputs
Korean letter level (가-힣)  
(Only the characters in the dataset)

조합된 글자 자체를 출력하면서 데이터 셋에 있는 글자만 사용


--- With DROPOUT ---

"""
from os.path import splitext
file_name = splitext(__file__)[0]
print("Running: ", file_name)


## Disable debugging logs
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


## Ready for data Pre-Processing

# Special letter

space = ' '
special_letters = [space]


# English data

big = [chr(i) for i in range(ord('A'), ord('Z')+1)]
small = [chr(i) for i in range(ord('a'), ord('z')+1)]

english_letter_list = big + small

# Add special letters
english_letter_list.extend(special_letters)

# Make index mapping
idx2english = dict(enumerate(english_letter_list, 1))
english2idx = {v: k for k, v in idx2english.items()}


# Read dataset
import numpy as np
import pandas as pd

df = pd.read_csv('data/full_data.csv', encoding='utf8')


# Korean data
hang = df['hang'].values

korean_letter_list = list(set([letter for sent in hang for letter in sent]))

# Make index mapping
idx2korean = dict(enumerate(korean_letter_list, 1))
korean2idx = {v: k for k, v in idx2korean.items()}


# Load X

roma = df['roma'].apply(lambda x: np.array([english2idx[letter] for letter in x]))
roma_df = pd.DataFrame(roma)
X = pd.DataFrame(roma_df['roma'].tolist()).values

# Replace nan to 0 
# Get index of nan, and make them 0
X[np.isnan(X)] = 0


# Load y

hang = df['hang'].apply(lambda x: np.array([korean2idx[letter] for letter in x]))
hang_df = pd.DataFrame(hang)
y = pd.DataFrame(hang_df['hang'].tolist()).values

# Replace nan to 0
# Get index of nan, and make them 0
y[np.isnan(y)] = 0

# one hot encoding
from keras.utils import np_utils
y = np_utils.to_categorical(y, num_classes=len(korean_letter_list)+1).reshape(y.shape[0], y.shape[1], len(korean_letter_list)+1)


# Split train & test & val set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1)


# ## Hyper Parameters

from keras.layers import recurrent

# Parameters for the model and dataset
TRAINING_SIZE = 50000
VOCAB_SIZE = 12
INVERT = True
HIDDEN_SIZE = 200
BATCH_SIZE = 100
LAYERS = 2
MAX_EPOCHS = 100
EMBEDDING_OUTPUT_SIZE = 128
MAX_OUTPUT_SENT_LENGTH = y.shape[1]
DROPOUT_RATE = 0.25

RNN = recurrent.GRU
stop_monitor = 'val_acc'
stop_delta = 0.0
stop_epochs = 20


# ## Build Model

# In[25]:


from keras.models import Sequential, load_model
from keras.layers import Dense, TimeDistributed, Activation, RepeatVector, Embedding, Dropout


print('Build Model...')

RNN = recurrent.GRU

model = Sequential()

model.add(Embedding(
    input_dim=len(english_letter_list)+1,  # 단어 갯수 + padding (1)
    output_dim=200,  # 출력 벡터
    input_length=X.shape[1]  # 입력 길이
))

model.add(RNN(HIDDEN_SIZE, return_sequences=True, input_shape=(X.shape[1], )))
model.add(RNN(HIDDEN_SIZE))

model.add(RepeatVector(MAX_OUTPUT_SENT_LENGTH))  # Maximum output length

for _ in range(LAYERS):
    model.add(RNN(HIDDEN_SIZE, return_sequences=True))
    model.add(Dropout(DROPOUT_RATE))

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