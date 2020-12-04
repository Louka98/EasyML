from flask import Flask
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


from sklearn.datasets import load_breast_cancer  #for testing

class logistic_regression:
    def __init__(self,solver , penalty , C):  #C is the hyperparameter for penalty power control
                                   #it is supposed to return the model parameters + accuracy of the model . these two has to be plotted (education aim)
        self.solver = solver
        self.penalty = penalty
        self.C = C
        self.model = LogisticRegression(solver =self.solver, penalty = self.penalty ,C = self.C)  
    def train(self , X_train, y_train):
    
       self.model = self.model.fit(X_train, y_train)  
       return self.model
       


    def predict(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        return classification_report(y_test,y_pred)

    