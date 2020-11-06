from flask import Flask
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_breast_cancer  #for testing

class logistic_regression:
    def __init__(self,solver , penalty , C,test_size,random_state, preprocessed_data):  #C is the hyperparameter for penalty power control
                                   #it is supposed to return the model parameters + accuracy of the model . these two has to be plotted (education aim)
        self.solver = solver
        self.penalty = penalty
        self.C = C
        self.preprocessed_data = preprocessed_data
        self.test_size = test_size
        self.random_state = random_state
        self.model = LogisticRegression()  

    @classmethod    
    def train(self):
        X = self.preprocessed_data.iloc[:, :-1].values
        y = self.preprocessed_data.iloc[:, -1].values 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)

  

        if ((self.solver == " ") | (self.penalty == " ")):
             #remember in preprocessing steps that the Sklearn doesnt accept string data , only numeric
             self.model = self.model.fit(X_train, y_train) 
             self.predict(X_test, y_test)
        else :
         
            solvers = ['newton-cg', 'lbfgs', 'liblinear']
            penalty = ['l2']
            c_values = [100, 10, 1.0, 0.1, 0.01] 
            grid = dict(solver=solvers,penalty=penalty,C=c_values)
            cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
            grid_search = GridSearchCV(estimator=self.model, param_grid=grid, n_jobs=-1, cv=cv, scoring='accuracy',error_score=0)
            grid_result = grid_search.fit(X, y)
                      # summarize results
            print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
            means = grid_result.cv_results_['mean_test_score']
            stds = grid_result.cv_results_['std_test_score']
            params = grid_result.cv_results_['params']
            final_output = []
            for mean, stdev, param in zip(means, stds, params):
                        final_output.append(mean, stdev, param)
            return final_output   
    @classmethod
    def predict(self, X_test,y_test ):
        predicted_classes = self.model.predict(X_test)
        accuracy = accuracy_score(y_test.flatten(),predicted_classes)  #comparison between real labels and predicted ones
        return  self.model.coef_ , accuracy  #weights + evaluation
             
if __name__ == '__main__':
    pass
#Add visualization
