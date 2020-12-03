from sklearn.decomposition import PCA



class PCA:  #for dimensionality reduciton

    def __init__(self,n_components): #important parametrs
        self.n_components = n_components
        self.model = PCA(n_components = self.n_components) #number of needed components (dimensions) to be displayed
    

    def train(self,data):
        self.model = self.model.fit(data) #fitting
        self.model.transform(data)
        return self.model, self.model.explained_variance_  
    
    