import re
from typing import List, Optional, Tuple
from numpy.core.numeric import cross
import tensorflow as tf
from tensorflow import keras
from enum import Enum
import numpy as np
from tensorflow.keras import layers
from tensorflow.python.framework.ops import pack_eager_tensors
from tensorflow.python.keras.engine.base_layer import Layer

class ModelTypes(Enum):
    binary = 1
    multi_class = 2
    multi_label = 3

class Loss(Enum):
    binary_crossentropy = 1
    categorical_crossentropy = 2

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


    def create_custom(self,layers: List[int], loss :Loss):
        '''Creates a custom model if all necessary parameters were given in the constructor.
        The layers list length will represent the amount of layers, and each element is the number of neurons in each layer.'''
        #TODO: exception if not all necessary values was given in init 
        try:
            self.model = keras.Sequential()
            self.model.add(keras.layers.Dense(layers[0], activation= self.hidden_act_func.name, input_shape = self.input_shape))
            for neurons in layers[1:-1]:
                self.model.add(keras.layers.Dense(neurons, activation= self.hidden_act_func.name))
            self.model.add(keras.layers.Dense(self.output_dim, activation= self.act_func.name)) #output layer
            if loss == Loss.binary_crossentropy:
                self.type = ModelTypes.multi_label
            elif loss == Loss.categorical_crossentropy:
                self.type = ModelTypes.multi_class
        except Exception as e:
            print(e)
        
    
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
    train_x, train_y = np.vstack((np.random.uniform(low=0., high=10., size=(1000,10)),np.random.uniform(low=11., high=20., size=(1000,10)))), np.hstack((np.ones(1000), np.zeros(1000)))
    
    model = ClassificationModel(input_shape= (train_x.shape[-1],), output_dim= 1, hidden_act_func=ActivationFunctions.relu, act_func=ActivationFunctions.sigmoid)

    layers = [20,20,20,20,20,1]
    model.create_custom(layers= layers, loss = Loss.binary_crossentropy)
    model.model.summary()
    hist = model.train(train_x,train_y, batch_size=3,val_split=0.2,epochs= 10, early_stopping=False)
    class_ones_res = model.predict(np.random.uniform(low=0., high=10., size=(2,10)))
    class_zeros_res = model.predict(np.random.uniform(low=11., high=20., size=(1,10)))
    print(class_ones_res)
    print(class_zeros_res)

    # train_x = np.vstack((np.random.uniform(low=0., high=10., size=(1000,10)),np.random.uniform(low=11., high=20., size=(1000,10)))) 
    
    # train_y = np.vstack((np.hstack((np.ones(1000).reshape(1000,1),np.zeros(1000).reshape(1000,1),np.zeros(1000).reshape(1000,1))), np.hstack((np.zeros(1000).reshape(1000,1),np.ones(1000).reshape(1000,1),np.zeros(1000).reshape(1000,1)))))
    # print(train_x.shape)
    # print(train_y.shape)
    # model = ClassificationModel(input_shape= (train_x.shape[-1],), output_dim=train_y.shape[-1],hidden_act_func=ActivationFunctions.relu, act_func=ActivationFunctions.softmax)
    # lays = [10,10,10,10,10,1]
    # model.create_custom( layers= lays, loss=Loss.categorical_crossentropy)
    # print(model.input_shape)
    # print(model.output_dim)
    # print(model.model.summary())
    # hist = model.train(train_x,train_y, batch_size=3,val_split=0.2,epochs= 10, early_stopping=False)
    # print(model.predict(np.random.uniform(low=0., high=10., size=(1,10))))
    # print(model.predict(np.random.uniform(low=11., high=20., size=(1,10))))

    #train_x, train_y = np.vstack((np.random.uniform(low=0., high=10., size=(1000,10)),np.random.uniform(low=11., high=20., size=(1000,10)))), np.hstack((np.ones(1000), np.zeros(1000)))
    # model = ClassificationModel(layers= 5, neurons= 20, input_shape= (train_x.shape[-1],))
    # model.create_template(type = ModelTypes.binary)
    # model.model.summary()
    # hist = model.train(train_x,train_y, batch_size=3,val_split=0.2,epochs= 10, early_stopping=False)
    # class_ones_res = model.predict(np.random.uniform(low=0., high=10., size=(2,10)))
    # class_zeros_res = model.predict(np.random.uniform(low=11., high=20., size=(1,10)))
    # print(np.around(class_ones_res))
    # print(np.around(class_zeros_res))