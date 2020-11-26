from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from numpy import nan
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn import datasets
from sklearn.impute import SimpleImputer

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
    def drop_nan(self,data):  #Drop row that contains NaN
        return data.dropna(inplace=True)
    def mean_nan(self,data):  #Replace each NaN by the  mean of its column
        return data.fillna(data.mean(), inplace=True)
    def count_nan(self,data): #returns the number of NaN in the DS
        return data.isnull().sum()
    def imputer(self): #should be used with pipeline 
        return SimpleImputer(missing_values=nan, strategy='most_frequent')





if __name__ == "__main__" :
    # wine = datasets.load_wine()
    # prep = preprocess()
    # dataset = pd.DataFrame(np.c_[wine['data'], wine['target']],
    #                  columns= wine['feature_names'] + ['target'])
    # prep.mean_nan(dataset)
    # print(dataset.isnull().sum())
    pass
    

    
     