"""
Readable 한 모델 결과를 보기 위한 스크립트

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


# Get original X
original_X_test = np.flip(X_test, axis=1)
original_X_test = [''.join([idx2english[j] for j in i if j != 0]) for i in original_X_test]

from keras.models import load_model
model_name_to_read = './models/GRU2GRU_consonant-vowel_LSTM_flip_checkpoint'
loaded_model = load_model(model_name_to_read)
# results = loaded_model.predict(X_test)
# argmax_result = np.argmax(results, axis=2)
# readable_results = [''.join([idx2korean[let] for let in one_result if let != 0]) for one_result in argmax_result]
#
# for x,y in zip(original_X_test, readable_results):
#     print(x, " : ", y)

custom_input = ['crong', 'krong', 'hello', 'derek', 'rob', 'dennis']
from keras.preprocessing.sequence import pad_sequences
custom_X = pad_sequences([[english2idx[letter] for letter in word] for word in custom_input], maxlen=X.shape[1], padding='post')

custom_X = np.flip(custom_X, axis=1)

custom_results = loaded_model.predict(custom_X)
custom_argmax_result = np.argmax(custom_results, axis=2)
custom_readable_results = [''.join([idx2korean[let] for let in one_result if let != 0]) for one_result in custom_argmax_result]


# Auto mata
from hangul import hangul

assemble = hangul.hangul.a


print('-----CUSTOM-----')
for x, y in zip(custom_input, custom_readable_results):
    print(x, ' : ', assemble(y))


print("Custom Input. You can split with ,")

for _ in range(0, 100):
    user_input = input('Input: ')
    if ',' in user_input:
        custom_input_X = user_input.split(',')
    else:
        custom_input_X = [user_input]

    custom_X = pad_sequences([[english2idx[letter] for letter in word] for word in custom_input_X], maxlen=X.shape[1],
                             padding='post')

    custom_X = np.flip(custom_X, axis=1)

    custom_results = loaded_model.predict(custom_X)
    custom_argmax_result = np.argmax(custom_results, axis=2)
    custom_readable_results = [''.join([idx2korean[let] for let in one_result if let != 0]) for one_result in
                               custom_argmax_result]

    for x, y in zip(custom_input_X, custom_readable_results):
        print(x,": ", assemble(y))

    print()