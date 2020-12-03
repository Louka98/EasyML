import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets


class KNN:
    def __init__(self,n_neighbors ,metric, weights): #important parametrs
        self.n_neighbors = n_neighbors
        self.metric = metric
        self.weigths = weights
        self.model = KNeighborsClassifier(n_neighbors = self.n_neighbors,metric=self.metric,weights=self.weigths)
    

    def train(self, X_train, y_train):
        self.model = self.model.fit(X_train, y_train) #fitting
        return self.model

    def predict(self ,X_test, y_test ):
        predicted_classes = self.model.predict(X_test)
        return metrics.accuracy_score(y_test, predicted_classes) #evaluation


        
if __name__ == "__main__":    
    pass
    # wine = datasets.load_wine()
    KNN = KNN(3,'euclidean','distance')
    # # KNN.train(X , y)
    # dataset = pd.DataFrame(np.c_[wine['data'], wine['target']],
    #                  columns= wine['feature_names'] + ['target'])
    
    # X = dataset.iloc[:, :-1].values
    # y = dataset.iloc[:, -1].values
    # KNN.train(X,y)     

    