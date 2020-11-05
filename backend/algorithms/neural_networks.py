from typing import Optional
from tensorflow import keras
from enum import Enum

from tensorflow.python.framework.ops import pack_eager_tensors

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
    
    def __init__(self, type : Optional[ModelTypes] = None, layers : int = 1 , neurons:int = 10, input_dim: int = 1, output_dim: int  = 2, act_func: Optional[ActivationFunctions]= None, hidden_act_func: Optional[ActivationFunctions]= None):
        self.type = type
        self.layers = layers
        self.neurons = neurons
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.act_func = act_func
        self.hidden_act_func = hidden_act_func

    @classmethod
    def create(self):
        #TODO: exception if not all necessary values was given in init 
        pass

    @classmethod
    def binary(self):
        pass
    
    @classmethod
    def multi_class(self):
        pass
    
    @classmethod
    def multi_label(self):
        pass

    def train():
        pass

    def predict():
        pass

if __name__ == '__main__':
    pass