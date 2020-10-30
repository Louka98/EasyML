remove from flask import Flask
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

#add upload dataset function


def SVM(data):
    x = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)
    svclassifier = SVC(kernel='linear')
    classifier = svclassifier.fit(X_train, y_train)
    y_pred = svclassifier.predict(X_test)
    return classification_report(y_test,y_pred) , (confusion_matrix(y_test,y_pred))
#Add visualization of output