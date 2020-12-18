from sklearn.clusters import KMeans
import matplotlib.pylot as plt
import numpy as np
import pandas as pd


def elbowvis()
    wcss=[]
    for i in range(1,30): 
         kmeans = KMeans(n_clusters=i, init ='k-means++', max_iter=300,  n_init=10,random_state=0 )
         kmeans.fit(data)
         wcss.append(kmeans.inertia_)

     

    plt.figure(figsize=(8,8))
    plt.plot(range(1,30),wcss)
    plt.title('The Elbow Method Graph')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()
