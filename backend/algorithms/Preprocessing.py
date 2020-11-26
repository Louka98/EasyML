from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn import datasets

class preprocess:
    def __init__(self):
        pass
    

    def normalize(self,data):
        scaler = preprocessing.MinMaxScaler()
        scaler.fit(data)
        data = pd.DataFrame(scaler.transform(data), index=data.index, columns=data.columns)
        return data
                

    def standarize(self,data):
        scaler = preprocessing.StandardScaler()
        scaler.fit(data)
        data = pd.DataFrame(scaler.transform(data), index=data.index, columns=data.columns)
        return data
    
    def categorical(self,data,categories):
        newdata=pd.get_dummies(data,columns=categories)
        
        return newdata
    def drop_nan(self,data):
        return data.dropna(inplace=True)
    def mean_nan(self,data):
        return data.fillna(data.mean(), inplace=True)




if __name__ == "__main__" :
    wine = datasets.load_wine()
    prep = preprocess()
    dataset = pd.DataFrame(np.c_[wine['data'], wine['target']],
                     columns= wine['feature_names'] + ['target'])
    prep.mean_nan(dataset)
   
    

    
     