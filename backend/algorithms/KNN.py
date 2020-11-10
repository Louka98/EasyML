import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets


class KNN:
    def __init__(self,n_neighbors ,metric, weights, test_size, preprocessed_data,random_state):
        self.n_neighbors = n_neighbors
        self.metric = metric
        self.weigths = weights
        self.test_size = test_size
        self.preprocessed_data = preprocessed_data
        self.random_state = random_state
        self.model = KNeighborsClassifier(n_neighbors = self.n_neighbors,metric = self.metric,weights=self.weigths)




    @classmethod
    def train(self):
        X = self.preprocessed_data.iloc[:, :-1].values
        y = self.preprocessed_data.iloc[:, -1].values 
        X_train, X_test, y_train, y_test = train_test_split(self.preprocessed_data.data, self.preprocessed_data.target, test_size=self.test_size, random_state=self.random_state)
        self.model = self.model.fit(X_train, y_train) 
        predicted_classes = self.model.predict(X_test)
        print("Accuracy:",metrics.accuracy_score(y_test, predicted_classes))


    @classmethod
    def predict(self):
        pass
if __name__ == "__main__":    
    wine = datasets.load_wine()
    KNN = KNN(3,'euclidean','distance', 0.3,wine, 1)



