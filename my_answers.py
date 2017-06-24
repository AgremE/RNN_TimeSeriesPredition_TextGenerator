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
    X = [series[i:i+window_size] for i in range(0,len(series)-window_size)]
    y = [series[window_size+i] for i in range(0,len(series) - window_size)]
        
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    # given - fix random seed - so we can all reproduce the same results on our default time series
    np.random.seed(0)
    # TODO: build an RNN to perform regression on our time series input/output data
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size,1)))
    model.add(Dense(1))


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    list_chara = list(text)
    english_chara = ['i', 's', ' ', 'e', 'y', 'h', 'c', 'l', 'p', 'a', 'n', 'd', 
                     'r', 'o', 'm', 't', 'w', 'f', 'x', '.', 'k', 'v', ',', 'u', 
                     'b', 'g', 'j', 'q', ':', 'z', ';', '!', '?']

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
    inputs= [text[i:i+window_size] for i in range(0,len(text)-window_size, step_size)]
    outputs= [text[i+window_size] for i in range(0,len(text)-window_size, step_size)]
    #outputs.shape = (len(outputs),1)
    return inputs,outputs
