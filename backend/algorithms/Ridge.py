from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import confusion_matrix

class Ridge:
    def  __init__(self,alpha):
        self.alpha=alpha
        self.model =RidgeClassifier( alpha = self.alpha)
    def train(self,X_train,y_train):
              self.model = self.model.fit(X_train, y_train) 
              return self.model , self.model.score(X_train, y_train)
       


    @classmethod
    def predict(self, X_test, y_test):
        ypred = self.model.predict(X_test)
        matrix = confusion_matrix(y_test, ypred)
        return matrix

