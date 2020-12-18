from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

class preprocess:
    def __init__(self):
        self.technique = None

    #NMin max scaler- normalization
    def normalize(data):
        scaler = preprocessing.MinMaxScaler()
        scaler.fit(data)
        data = pd.DataFrame(scaler.transform(data), index=data.index, columns=data.columns)
        return data
                
    # Z-score Standaratztion
    def standarize(data):
        scaler = preprocessing.StandardScaler()
        scaler.fit(data)
        data = pd.DataFrame(scaler.transform(data), index=data.index, columns=data.columns)
        return data
    # Converting categorical datas to numeric data
    def categorical(data,categories):
        newdata=pd.get_dummies(data,columns=categories)
        
        return newdata
