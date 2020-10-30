from flask import Flask
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def logistic_regression(data):  #it is supposed to return the model parameters + accuracy of the model . these two has to be plotted (education aim)
    model = LogisticRegression()  
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    model.fit(X, y) 
    predicted_classes = model.predict(X)
    accuracy = accuracy_score(y.flatten(),predicted_classes)  #comparison between real labels and predicted ones
    return  model.coef_ , accuracy   #outputs

#Add visualization