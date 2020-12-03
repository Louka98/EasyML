from sklearn.decomposition import PCA
from sklearn import datasets
import numpy as np
import pandas as pd

class Principal_Component_Analysis:  #for dimensionality reduciton

    def __init__(self,n_components): #important parametrs
        self.n_components = n_components
        self.model = PCA(n_components = self.n_components) #number of needed components (dimensions) to be displayed
    

    def train(self,data):
        self.model = self.model.fit(data) #fitting
        self.model.transform(data)
        print(self.model.components_)  #selected components to keep
        return data
    

if __name__ == "__main__":    
    pass
    #  wine = datasets.load_wine()
    #  dataset = pd.DataFrame(np.c_[wine['data'], wine['target']],
    #                                       columns= wine['feature_names'] + ['target'])
    #  model = Principal_Component_Analysis(3)
    #  model.train(dataset)
     