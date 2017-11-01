
# coding: utf-8

# # Sequence to Sequence
# 
# ## Inputs
# Korean letter level (가-힣)  
# (Only the characters in the dataset)
# 
# 조합된 글자 자체를 출력하되, 데이터 셋에 있는 글자만 사용

# ## Ready for data Pre-Processing

# In[11]:


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

df = pd.read_csv('data/demo_data.csv', encoding='utf8')
del df['Unnamed: 0']


# Korean data
hang = df['hang'].values

korean_letter_list = list(set([letter for sent in hang for letter in sent]))

# Make index mapping
idx2korean = dict(enumerate(korean_letter_list, 1))
korean2idx = {v: k for k, v in idx2korean.items()}


# ## Data Pre-processing

# In[19]:


# Load X

roma = df['roma'].apply(lambda x: np.array([english2idx[letter] for letter in x]))
roma_df = pd.DataFrame(roma)
X = pd.DataFrame(roma_df['roma'].tolist()).values

# Replace nan to 0 
# Get index of nan, and make them 0
X[np.isnan(X)] = 0
print(X)


# In[21]:


# Load y

hang = df['hang'].apply(lambda x: np.array([korean2idx[letter] for letter in x]))
hang_df = pd.DataFrame(hang)
y = pd.DataFrame(hang_df['hang'].tolist()).values

# Replace nan to 0
# Get index of nan, and make them 0
y[np.isnan(y)] = 0
print(y)
print(y.shape)

# one hot encoding
from keras.utils import np_utils
y = np_utils.to_categorical(y, num_classes=len(korean_letter_list)+1).reshape(300, 12, len(korean_letter_list)+1)
print(y.shape)


# In[22]:


# Split train & test & val set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1)


# ## Hyper Parameters

# In[24]:


from keras.layers import recurrent

# Parameters for the model and dataset
TRAINING_SIZE = 50000
VOCAB_SIZE = 12
INVERT = True
HIDDEN_SIZE = 200
BATCH_SIZE = 100
LAYERS = 2
MAX_EPOCHS = 1000
EMBEDDING_OUTPUT_SIZE = 128
MAX_SENT_LENGTH = X.shape[1] + 1

RNN = recurrent.GRU
stop_monitor = 'val_acc'
stop_delta = 0.0
stop_epochs = 20


# ## Build Model

# In[25]:


from keras.models import Sequential
from keras.layers import Dense, TimeDistributed, Activation, RepeatVector, Embedding, Dropout

def build_model(
    embedding_input_dim,
    embedding_output_dim,
    embedding_input_length,
    hidden_size,
    maximum_output_length,
    encoder_layer_count,
    dropout_rate,
    output_classes_count,
    rnn_layer,
    summary_type=False):
    
    print('Build Model...')
    
    RNN = rnn_layer
    
    model = Sequential()
    
    model.add(Embedding(
        input_dim=embedding_input_dim,
        output_dim=embedding_output_dim,
        input_length=embedding_input_length
    ))
    
    model.add(RNN(hidden_size, return_sequences=True, input_shape=(maximum_input_length, )))
    model.add(RNN(hidden_size))
    
    model.add(RepeatVector(maximum_output_length))  # Maximum output length
    
    for _ in range(encoder_layer_count):
        model.add(RNN(hidden_size, return_sequences=True))
        model.add(Dropout(dropout_rate))
        
    model.add(TimeDistributed(Dense(output_classes_count)))
    model.add(Activation('softmax'))
    
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )
    
    if summary_type is False:
        pass
    elif str(summary_type).lower() == 'svg':
        viz_model(model)
    else:
        model.summary()
        
    return model

print('Done')

