from flask import Flask
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

class decision_tree:

 def __init__(self, criterion, max_depth) : # complet parameters of the model
     self.criterion = criterion
     self.max_depth = max_depth
     self.model = DecisionTreeClassifier(criterion = self.criterion, max_depth = self.max_depth)


    #it is supposed to return the model parameters + accuracy of the model . these two has to be plotted (education aim)
 def train(self,X_train, y_train):
    self.model = self.model.fit(X_train, y_train)

    return self.model
     
      
 def predict(self, X_test, y_test):
    y_pred = self.model.predict(X_test)
    return metrics.accuracy_score(y_test, y_pred)



if __name__ == '__main__':
    pass
