from math import nan
from typing import List
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

class CustomPreprocess:

    def __init__(self):
        self.technique = None

    def normalize(self, data):
        for x in data.columns:
            if data[x].dtypes == float:
                data[x]=((data[x]-data[x].min())/(data[x].max()-data[x].min()))
        
        return data

    def standatize(self, data):
        for x in data.columns:
            if data[x].dtypes == float:
                data[x]=((data[x]-data[x].mean())/(data[x].std()))
        
        return data

    def onehotencoder(self,data,categ_col_names: List[str]):
        categ_col_names = categ_col_names[0].split(',')
        for x in data.columns:
            if x in categ_col_names:
                le = preprocessing.LabelEncoder()
                encoded = le.fit_transform(data[x])
                one_hot = to_categorical(encoded)
                new_names = []
                for i in range(one_hot.shape[-1]):
                    new_names.append(f'{x}_{i}')
                data = data.drop(x ,axis = 1)
                df = pd.DataFrame(one_hot, columns= new_names)
                print(df)
                data[new_names] = one_hot
        
        return data

    def filter_nan(self, data):
        '''Removes the rows with nan values in them'''
        for x in data.columns:
            data[x] = data[x].apply(lambda x: x if x != "" else None )
        return data.dropna()

    def type_convert(self, data, target_column, categ_col_names):
        '''try to convert the rows of the data to float, skipping the categorical datas'''
        categ_col_names = categ_col_names[0].split(',')
        for x in data.columns:
            try:
                print(categ_col_names)
                print(target_column)
                if x not in categ_col_names and x != target_column:
                    print(x)
                    data[x] = data[x].astype(float)
            except Exception as e:
                print(e)
        
        return data

    def t_t_split(self,data, target_column, test_size, loss, output_dim):

        X = data.drop(target_column, axis = 1)
        y = data[target_column]
        if output_dim > 1 and loss == "binary_crossentropy":
            mle = preprocessing.MultiLabelBinarizer()
            y = [x.split(',') for x in y]
            y = mle.fit_transform(y)
        else:
            le = preprocessing.LabelEncoder()
            encoded = le.fit_transform(y)
            if output_dim == 1:
                y = encoded
            elif output_dim > 1 and loss == "categorical_crossentropy":
                y = to_categorical(encoded)

        return train_test_split(X, y, test_size = test_size)


    def transform(self, data, target_column: str, categ_col_names: List[str], test_size:float, loss:str = None, output_dim:str = None):
        data = pd.DataFrame(data[1:], columns=data[0])
        data = self.filter_nan(data)
        data = self.type_convert(data,target_column, categ_col_names)
        data = self.normalize(data)
        data = self.onehotencoder(data,categ_col_names)
        print('-----transformed data-----')
        print(data)
        print('-----END transformed data-----')
        print(data.dtypes)
        print("--------END Types-------")
    
        if loss and output_dim:
            ret = self.t_t_split(data, target_column, test_size, loss, output_dim)
            X_train, X_test, y_train, y_test = ret
            print(X_train)
            print(np.array(X_train))
            print(X_test)
            print(y_train)
            print(y_test)
            
            return ret
        
        return data
        