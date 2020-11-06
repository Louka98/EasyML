from flask import Flask
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

class decision_tree:

 def __init__(self, criterion, max_depth, test_size,random_state, preprocessed_data) : # complet parameters of the model
     self.criterion = criterion
     self.max_depth = max_depth
     self.test_size = test_size
     self.random_state = random_state
     self.preprocessed_data = preprocessed_data
     self.model = DecisionTreeClassifier(criterion = self.criterion, max_depth = self.max_depth)


    #it is supposed to return the model parameters + accuracy of the model . these two has to be plotted (education aim)
@classmethod   
def train(self):
    X = self.preprocessed_data.iloc[:, :-1].values
    y = self.preprocessed_data.iloc[:, -1].values  #remember in preprocessing steps that the Sklearn doesnt accept string data , only numeric
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)
    self.model = self.model.fit(X_train, y_train)
    y_pred = self.model.predict(X_test)
    return metrics.accuracy_score(y_test, y_pred)
     
      
@classmethod
def predict(self, X_test, y_test):
    pass



if __name__ == '__main__':
    pass
#Add visualization