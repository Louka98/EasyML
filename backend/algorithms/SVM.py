import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import datasets
#add upload dataset function

class SVM: 

    def __init__(self, C,kernel , gamma,shrinking): # à  continuer
       self.C= C
       self.kernel = kernel
       self.gamma = gamma
       self.shrinking = shrinking
       self.model = SVC(kernel=self.kernel, gamma = self.gamma, C= self.C, shrinking = self.shrinking)


    
    def train(self , X_train, y_train):
    #    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = self.test_size)
       self.model = self.model.fit(X_train, y_train)   # à continuer d'ici
       return self.model
       


    def predict(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        return classification_report(y_test,y_pred) , (confusion_matrix(y_test,y_pred))

    def visualize(self , X_train):
        support_vectors = self.model.support_vectors_
        plt.scatter(X_train[:,0], X_train[:,1])
        plt.scatter(support_vectors[:,0], support_vectors[:,1], color='red') #red to color the boundary
        plt.title('separated vectors ')
        plt.xlabel('X1')
        plt.ylabel('X2')
        plt.show()

if __name__ == "__main__":    
    
    # wine = datasets.load_wine()
    # model = SVM(C = 0.01 , kernel ='linear', gamma = 0.1,shrinking=False)
    # dataset = pd.DataFrame(np.c_[wine['data'], wine['target']],
    #                  columns= wine['feature_names'] + ['target'])
    
    # X = dataset.iloc[:, :-1].values
    # y = dataset.iloc[:, -1].values
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

    # # model.train(X_train,y_train) 
    # # model.predict(X_test,y_test)  
    # # model.visualize(X_train)  





