import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras
import string


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = []
    y = []
    for i in range(len(series)-window_size):
        data_input = []
        for input_ind in range(window_size):
            data_input.append(series[input_ind+i])
        X.append(data_input)
        y.append(series[i+window_size])
        
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    np.random.seed(0)
    # TODO: build an RNN to perform regression on our time series input/output data
    model = Sequential()
    model.add(LSTM(240, return_sequences=True, input_shape=(7,1),dropout=0.2))
    model.add(LSTM(240,return_sequences=True,dropout=0.2))
    model.add(LSTM(240,return_sequences=True,dropout=0.1))
    model.add(LSTM(300))
    model.add(Dense(1,activation='tanh'))


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    list_chara = list(text)
    english_chara = ['i', 's', ' ', 'e', 'y', 'h', 'c', 'l', 'p', 'a', 'n', 'd', 
                     'r', 'o', 'm', 't', 'w', 'f', 'x', '.', 'k', 'v', ',', 'u', 
                     'b', 'g', '-', "'", 'j', 'q', ':', '1', '8', '(', ')', 'z', 
                     ';', '"', '!', '?', '5', '4', '7', '2', '9', '0', '3', '6']

    # remove as many non-english characters and character sequences as you can 
    for i in range(len(list_chara)):
        if not (list_chara[i] in english_chara):
            text = text.replace(list_chara[i],' ')
    
    # shorten any extra dead space created above
    text = text.replace('  ',' ')

    # remove as many non-english characters and character sequences as you can 


### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    for i in range(len(text)-step_size):
        inputs.append(text[i:window_size+i])
        outputs.append(text[i+window_size+1])
        i = i + step_size
        if (i + window_size) > len(text):
            break
    inputs = np.asarray(inputs)
    #print(inputs.shape)
    #inputs.shape = (np.shape(inputs[0:2]))
    outputs = np.asarray(outputs)
    #outputs.shape = (len(outputs),1)
    return inputs,outputs
