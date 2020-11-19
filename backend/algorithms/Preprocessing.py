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

    def normalize(data):
        for x in data.columns:
            if data[x].dtypes == float:
                data[x]=((data[x]-data[x].min())/(data[x].max()-data[x].min()))
        return data

    def standatize(data):
        for x in data.columns:
            if data[x].dtypes == float:
                data[x]=((data[x]-data[x].mean())/(data[x].std()))
        return data

    def onehotencoder(data,categories):
       
        categories= categories
        one_hot=OneHotEncoder()
        transformer= ColumnTransformer([("one_hot",one_hot,categories)],remainder='passthrough')
        transformed_X= transformer.fit_transform(data)
        transformed_X=pd.DataFrame(transformed_X)
        return transformed_X
    
    