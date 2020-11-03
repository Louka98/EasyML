from typing import List, Optional, Tuple
import tensorflow as tf
from tensorflow import keras
from enum import Enum
import numpy as np
from tensorflow.python.framework.ops import pack_eager_tensors
from tensorflow.python.keras.engine.base_layer import Layer

class ModelTypes(Enum):
    binary = 1
    multi_class = 2
    multi_label = 3

class ActivationFunctions(Enum):
    relu = 1
    selu = 4
    sigmoid = 2 #for binary and multi label
    softmax = 3 #multi class


class ClassificationModel:
    
    def __init__(self, type : Optional[ModelTypes] = None,
    layers : int = 1 ,
    neurons:int = 10,
    input_shape: tuple = (1,),
    output_dim: int  = 1,
    act_func: Optional[ActivationFunctions]= None,
    hidden_act_func: Optional[ActivationFunctions]= None,
    dropout : int = None):

        self.type = type
        self.layers = layers
        self.neurons = neurons
        self.input_shape = input_shape
        self.output_dim = output_dim
        self.act_func = act_func
        self.hidden_act_func = hidden_act_func
        self.dropout = dropout
        self.model = None


    def create(self):
        #TODO: exception if not all necessary values was given in init 
        pass
    
    def binary(self):
        '''Creates a sequential keras model'''
        self.model = keras.Sequential()

        self.model.add(keras.layers.Dense(self.neurons, activation= 'relu', input_shape = self.input_shape)) #input layer
        for i in range(self.layers - 1):
            self.model.add(keras.layers.Dense(self.neurons, activation= 'relu')) #hidden layers
            if self.dropout:
                self.model.add(keras.layers.Dropout(0.1))
        self.model.add(keras.layers.Dense(1, activation= 'sigmoid')) #output layer
        self.type = ModelTypes.binary
        
    
    def multi_class(self):
        pass
    
    def multi_label(self):
        pass

    def train(self, train_x: np.ndarray, train_y: np.ndarray,
            batch_size:int = 128, val_split = 0.1, epochs: int = 20, early_stopping: bool = True): #data_x is a [[1,2,3,4 ...],[...]...] and data_y = [0,1,0,1..] are the labels in order
        '''trains the model'''
        
        self.model.compile(optimizer = 'adam', loss='binary_crossentropy')
        if early_stopping:
            callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights= True)
            history = self.model.fit(train_x, train_y,
                        batch_size=batch_size,
                        epochs=epochs,
                        validation_split= val_split,
                        shuffle=True,
                        verbose=1,
                        callbacks = [callback])
        else:
            history = self.model.fit(train_x, train_y,
                        batch_size=batch_size,
                        epochs=epochs,
                        validation_split= val_split,
                        shuffle=True,
                        verbose=1)

        return history

    def save_model(self, path):
        pass

    def load_model(self, path):
        pass

    def predict(self, data:np.ndarray):
        return self.model.predict(data)

if __name__ == '__main__':
    train_x, train_y = np.arange(100).reshape(5, 20), np.ones(5)
    model = ClassificationModel(layers= 10, neurons= 20, input_shape= (train_x.shape[-1],))
    model.binary()
    hist = model.train(train_x,train_y, batch_size=3,val_split=0.2,epochs= 10, early_stopping=False)
    print(model.predict(np.arange(20).reshape(1,20)))
