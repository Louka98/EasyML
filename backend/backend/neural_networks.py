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
    
    def create_template(self, type : ModelTypes):
        '''Creates a sequential keras model for binary or multi class or multi label classification'''
        self.model = keras.Sequential()

        self.model.add(keras.layers.Dense(self.neurons, activation= 'relu', input_shape = self.input_shape)) #input layer
        for i in range(self.layers - 1):
            self.model.add(keras.layers.Dense(self.neurons, activation= 'relu')) #hidden layers
            if self.dropout:
                self.model.add(keras.layers.Dropout(0.1))
        
        if type == ModelTypes.binary:
            self.model.add(keras.layers.Dense(self.output_dim, activation= 'sigmoid')) #output layer
            self.type = ModelTypes.binary
        elif type == ModelTypes.multi_class:
            self.model.add(keras.layers.Dense(self.output_dim, activation= 'softmax')) #output layer
            self.type = ModelTypes.multi_class 
        elif type == ModelTypes.multi_label:
            self.model.add(keras.layers.Dense(self.output_dim, activation= 'sigmoid')) #output layer
            self.type = ModelTypes.multi_label   

    
    def train(self, train_x: np.ndarray, train_y: np.ndarray,
            batch_size:int = 128, val_split = 0.1, epochs: int = 20, early_stopping: bool = True): #data_x is a [[1,2,3,4 ...],[...]...] and data_y = [0,1,0,1..] are the labels in order
        '''trains the model'''
        if self.type == ModelTypes.binary or self.type == ModelTypes.multi_label:
            self.model.compile(optimizer = 'adam', loss='binary_crossentropy')
        elif self.type == ModelTypes.multi_class:
            self.model.compile(optimizer = 'adam', loss='categorical_crossentropy')

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
    pass
