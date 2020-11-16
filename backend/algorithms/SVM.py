import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

#add upload dataset function

class SVM: 

    def __init__(self, C,kernel , gamma,shrinking, test_size,random_state): # à  continuer
       self.C= C
       self.kernel = kernel
       self.gamma = gamma
       self.shrinking = shrinking
       self.test_siz = test_size
       self.random_state = random_state
       self.model = SVC(kernel=self.kernel, gamma = self.gamma, C= self.C, shrinking = self.shrinking)


    @classmethod
    def train(self , X_train, y_train):
    #    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = self.test_size)
       self.model = self.model.fit(X_train, y_train)   # à continuer d'ici
       return self.model
       


    @classmethod
    def predict(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        return classification_report(y_test,y_pred) , (confusion_matrix(y_test,y_pred))




if __name__ == "__main__":
    pass
#Add visualization of output