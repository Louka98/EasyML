import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

class Random_forest:
    def  __init__(self,nb_estimators,random_state):
        self.nb_estimators=nb_estimators  #important parameter, number of trees in the random forest
        self.random_state = random_state
        self.model = RandomForestRegressor(n_estimators=self.nb_estimators, random_state=self.random_state)
 
    def train(self, X_train,y_train):
        self.model = self.model.fit(X_train, y_train) #train the model on our dataset
        return self.model
       

    def predict_(self, X_test, y_test):
        ypred = self.model.predict(X_test)
        #In case of classification it should return the confusion matrix
        print(confusion_matrix(y_test,ypred))
        print(classification_report(y_test,ypred))
        print(accuracy_score(y_test, ypred))
        #in case of regression it should return this
        return  metrics.mean_absolute_error(y_test, ypred) , metrics.mean_squared_error(y_test, ypred) #MAE and MSE respectivly

if __name__ == '__main__':
 pass


# # Convert to png using system command (requires Graphviz)
#     from subprocess import call
#     call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])
