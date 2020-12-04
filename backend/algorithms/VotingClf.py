from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import  VotingClassifier
from sklearn.metrics import accuracy_score 
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVC 
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris 






class Voting:
    def __init__(self):
         self.L = LogisticRegression(solver ='lbfgs',  
                                     multi_class ='multinomial',  
                                     max_iter =50)
         self.D = DecisionTreeClassifier()
         self.S = SVC(gamma ='auto', probability = True)

         self.model = VotingClassifier(estimators = [("LR",self.L),("SVC",self.S),("DTC",self.D)], voting='soft') #try with hard
    def train(self , X_train, y_train):
       self.model = self.model.fit(X_train, y_train)   # à continuer d'ici
       return self.model
       


    def predict(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        return print(accuracy_score(y_test, y_pred))

if __name__ =="__main__":
    pass
    # iris = load_iris() 
    # X = iris.data[:, :4] 
    # Y = iris.target
    
    # X_train, X_test, y_train, y_test = train_test_split(X,  
    #                                                 Y,  
    #                                                 test_size = 0.20,  
    #                                                 random_state = 42) 
    # model = Voting()
    # X_scaled = preprocessing.scale(X_train)
    # model.train(X_scaled,y_train) 
    # model.predict(X_test,y_test)  


