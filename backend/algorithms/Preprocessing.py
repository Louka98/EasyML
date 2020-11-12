from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing

class preprocess:
    def __init__(self):
        self.technique = None

    def normalize(data):
        for x in data.columns:
            if data[x].dtypes == float:
                data[x]=((data[x]-data[x].min())/(data[x].max()-data[x].min()))
        return data

    def standatize(data):
        for x in data.columns:
            if data[x].dtypes == float:
                data[x]=((data[x]-data[x].mean())/(data[x].std()))
        return data

