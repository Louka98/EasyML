from flask import Flask
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier



def decision_tree(data):  #it is supposed to return the model parameters + accuracy of the model . these two has to be plotted (education aim)
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values  #remember in preprocessing steps that the Sklearn doesnt accept string data , only numeric 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=41)
    clf = DecisionTreeClassifier(criterion="gini", max_depth=3)
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return metrics.accuracy_score(y_test, y_pred)


#Add visualization