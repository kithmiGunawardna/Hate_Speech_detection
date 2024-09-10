import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import numpy as np
import pickle

__oversampled_df = None
__tokenizer = None
__model = None
__MAX_SEQUENCE_LENGTH = 250
__MAX_NB_WORDS = 50000


def load_dataset():
    global __oversampled_df
    __oversampled_df = pd.read_csv("C:\\Local Disk D\\Sliit\\4 year\\reserch\\campus research\\hate speech detection\\server\\artipact\\df.csv")

def load_model():
    global __model
    __model = pickle.load(open("C:\\Local Disk D\\Sliit\\4 year\\reserch\\campus research\\hate speech detection\\server\\artipact\\model.pkl", 'rb'))


def tokanization():
    global __oversampled_df ,__tokenizer
    
    __tokenizer = Tokenizer(num_words=__MAX_NB_WORDS)
    __tokenizer.fit_on_texts(__oversampled_df['tweet'].values)
    word_index = __tokenizer.word_index


def prediction(sentence):
    
    global __tokenizer 
    lables =['hate speech','offensive language','neither']
    X = __tokenizer.texts_to_sequences(sentence)
    X = pad_sequences(X, maxlen=__MAX_SEQUENCE_LENGTH)
    output=__model.predict(X)
    print(output,lables[np.argmax(output)],sentence,"\n")
    return lables[np.argmax(output)]



if __name__ =='__main__' :
    load_dataset()
    tokanization()
    load_model()
    prediction(["you stupid"])