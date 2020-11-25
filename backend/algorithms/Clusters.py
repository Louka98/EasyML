from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import OPTICS
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import MeanShift
from sklearn.cluster import SpectralClustering
from sklearn.metrics import silhouette_score
import numpy as np


class clustering:
    
    def __init__(self):
        self.model = None
        
    def nclusters(data):
        scores=[]
        for x in range(2,20):
            kmeans=KMeans(n_clusters=x)
            kmeans.fit(data)
            score = silhouette_score(data, kmeans.labels_, metric='euclidean')
            scores.append(score)
        return np.argmax(scores)+2
        
        
        
    def Kmeans(self, n_clusters=3):
       self.model= KMeans(n_clusters=n_clusters) #creating model
        
                        
    def Dbscan(self, eps = 0.3, min_samples = 10):
        self.model=DBSCAN(eps=eps,min_samples=min_samples) #creating model
        
    def agg_cluster(self,n_clusters=3,linkage):
        self.model=AgglomerativeClustering(n_clusters=n_clusters, linkage=linkage)
        
    def ms(self,bandwidth=2):
        self.model=MeanShift(bandwidth=bandwidth)
        
    def sc(self,n_clusters=3):
        self.model=SpectralClustering(n_clusters=n_clusters)

        
    def train(self,data):
        self.model.fit(data)
        data['Labels'] = self.model.labels_     #Result
        return data
    
    def pred(self,ex):
        y=self.model.predict(ex)
        return y
        
        
