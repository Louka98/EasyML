import numpy as np
import pandas as pd
from sklearn.clusters import KMeans
import matplotlib.pyplot as plt
def visualize()
    scores=[]
    for x in range(2,20):
            kmeans=KMeans(n_clusters=x)
            kmeans.fit(data)
            score = silhouette_score(data, kmeans.labels_)
            scores.append(score)

     


    plt.figure(figsize=(8,8))
    plt.plot(range(2,20),scores)
    plt.title('The Silhoutte score')
    plt.xlabel('Number of clusters')
    plt.ylabel('Score')
    plt.show()
    print(np.argmax(scores)+2)
