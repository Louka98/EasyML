from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

class Ridge:
    def  __init__(self,alpha):
        self.alpha=alpha  #alpha is the parameter that has the strongest impact in his model
        self.model =RidgeClassifier( alpha = self.alpha)
    def train(self, X_train,y_train):
            self.model = self.model.fit(X_train, y_train) #train the model on our dataset
            return self.model , self.model.score(X_train, y_train) #how much the model is confidence about the relationship between features and labels
       

    def predict_(self, X_test, y_test):
        ypred = self.model.predict(X_test)
        matrix = confusion_matrix(y_test, ypred)
        return matrix

if __name__ == '__main__':
    pass
    # model = Ridge(0.1)

    # x, y = make_classification(n_samples=5000, n_features=10, 
    #                        n_classes=3, 
    #                        n_clusters_per_class=1)
    # xtrain,xtest, ytrain,  ytest = train_test_split(x, y, test_size=0.15)
    # print(model.train(xtrain,ytrain))
    # print(model.predict_(xtest,ytest))