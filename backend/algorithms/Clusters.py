from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import OPTICS
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import MeanShift
from sklearn.cluster import SpectralClustering
import numpy as np


# Kmeans
def Kmeans(data):

    kmeans= KMeans(n_clusters=3) #creating model
    kmeans.fit(data)             #Fitting

    data['Labels'] = kmeans.labels_ #Result
    return data

def ClusteringModel():
    model: None

    def Dbs(eps, minsamp):
        model = DBSCAN(eps=0.3,min_samples=10)

    #
    #
    #
    def train(data):
        model.fit(data)
        data['Labels'] = model.labels_     #Result
        return data

    def predict(data):
        pass

#DBSCAN
def Dbscan(data):
    db=DBSCAN(eps=0.3,min_samples=10) #creating model
    db.fit(data)                   #model  
    
    data['Labels'] = db.labels_     #Result
      
    return data
 
def agg_cluster(data):
    ac=AgglomerativeClustering()
    ac.fit(data)
    
    data['Labels']= ac.labels_
    return data

def ms(data):
    ms=MeanShift(bandwidth=2)
    ms.fit(data)
    
    data["Labels"]=ms.labels_
    return data

def sc(data):
    sc=SpectralClustering(n_clusters=3)
    sc.fit(data)
    
    data["Labels"]= sc.labels_
    return data

def optics(data):
    op=OPTICS()
    op.fit(data)
    data["Labels"]=op.labels_
    return data