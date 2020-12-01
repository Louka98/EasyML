from backend.neural_networks import *
from algorithms.Clusters import clustering
import traceback
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy.lib.type_check import imag
import seaborn as sns

cluster_alg_names = ['kmeans']

def init_model(**kwargs):
    '''This function can initialize the models (any model), the parameters are passed as strings from the body of the requests'''
    
    model = None
    try:
        if kwargs['model_type'] == 'nn_custom':

            hidden_act_func = ActivationFunctions[kwargs['hidden_act_func']]
            act_func = ActivationFunctions[kwargs['act_func']]
            model = ClassificationModel(input_shape= kwargs['input_shape'], output_dim= kwargs['layers'][-1], hidden_act_func=ActivationFunctions.relu, act_func=ActivationFunctions.sigmoid)
            model.create_custom(layers= kwargs['layers'], loss = Loss[kwargs['loss']])

        if kwargs['model_type'] in cluster_alg_names:

            model = clustering()
            if kwargs['model_type'] == 'kmeans':
                try:
                    n_clusters = kwargs['n_clusters']
                except KeyError:
                    n_clusters, sil_scores, wcss = model.nclusters(kwargs['dataset'])

                model.kmeans(n_clusters=n_clusters)

        if kwargs['model_type'] == 'nn_binary_classification':

            model = ClassificationModel(layers = kwargs['layers'], neurons=kwargs['neurons'], input_shape=kwargs['input_shape'])
            model.create_template(type=ModelTypes.binary)

        return model
    
    except Exception as e:
        traceback.print_exc()
        
        return None

def train_model(model,train_x,train_y,test_x,test_y,**kwargs):
    '''This function can train any model, the parameters are passed as strings from the body of the requests'''
    
    try:
        hist = {}
        if isinstance(model, ClassificationModel):
            hist = model.train(train_x,train_y,test_x,test_y,batch_size=kwargs['batch_size'],epochs= kwargs['epochs'], early_stopping=kwargs['early_stopping']) #instead of val split val_split=0.2
            
        if isinstance(model, clustering):
            
            model = model.train(train_x)
            hist['labels'] = [int(x) for x in model.labels_]
            hist['cluster_centers'] = [[float(y) for y in x] for x in model.cluster_centers_]
            hist['interia'] = float(model.inertia_)
            hist['n_iter'] = int(model.n_iter_)
        return hist

    except Exception as e:
        traceback.print_exc()
        
        return None

def create_plot(model_type:str, hist, data = None):
    
    figsize = 5

    if model_type == 'nn_custom':
        fig = Figure(figsize=(figsize* 1.3,figsize*2))
        canvas = FigureCanvas(fig)

        print(hist)

        x = np.linspace(0, len(hist['loss']) -1, num = len(hist['loss']), dtype= np.int)

        loss = fig.add_subplot(2,1,1)
        loss.set_title('Loss')
        loss.plot(x, hist['loss'], label = 'loss', color = 'red')
        loss.plot(x, hist['val_loss'], label = 'val_loss', color = 'blue')
        loss.set_xlabel('epochs')
        loss.set_ylabel('loss')
        loss.legend()

        acc = fig.add_subplot(2,1,2)
        acc.set_title('Accuracy')
        acc.plot(x, hist['acc'], label = 'accuracy', color = 'red')
        acc.plot(x, hist['val_acc'], label = 'validation accuracy', color = 'blue')
        acc.set_xlabel('epochs')
        acc.set_ylabel('accuracy')
        acc.legend()
        #fig.subplots_adjust(hspace = 0.3)

        canvas.draw()       # draw the canvas, cache the renderer

        width, height = fig.get_size_inches() * fig.get_dpi()
        width, height = int(width), int(height)
        image = np.fromstring(canvas.tostring_rgb(), dtype='uint8').reshape(height,width,3)
        print('IMAGE_______')
        #print(image)
        print(image.shape)
        print(width)
        print(height)
        #plt.imshow(image)
        #plt.show()

        return image.tolist(), height, width

    if model_type == 'kmeans':
        hist['labels']
        data
        
        fig = Figure(figsize=(figsize* 1.3,figsize*2))
        canvas = FigureCanvas(fig)
        x = np.linspace(0, len(hist['sil_score']) -1, num = len(hist['sil_score']), dtype= np.int)

        sil_score = fig.add_subplot(2,1,1)
        sil_score.set_title('Silhouette scores')
        sil_score.plot(x, hist['sil_score'], label = 'sil score', color = 'red')
        sil_score.set_xlabel('number of clusters')
        sil_score.set_ylabel('silhouette score')
        sil_score.legend()

        wcss = fig.add_subplot(2,1,2)
        wcss.set_title('Elbow Method Graph')
        wcss.plot(x, hist['wcss'], label = 'wcss', color = 'red')
        wcss.set_xlabel('number of clusters')
        wcss.set_ylabel('WCSS')
        wcss.legend()
        #fig.subplots_adjust(hspace = 0.3)

        canvas.draw()       # draw the canvas, cache the renderer

        width, height = fig.get_size_inches() * fig.get_dpi()
        width, height = int(width), int(height)
        image = np.fromstring(canvas.tostring_rgb(), dtype='uint8').reshape(height,width,3)
        print('IMAGE_______')
        #print(image)
        print(image.shape)
        print(width)
        print(height)
        #plt.imshow(image)
        #plt.show()

        pairplot = sns.pairplot(data, hue = 'labels')
        fig2 = pairplot.fig
        fig2.set_size_inches(12,10)
        canvas2 = FigureCanvas(fig2)
        canvas2.draw()
        width2, height2 = fig2.get_size_inches() * fig2.get_dpi()
        width2, height2 = int(width2), int(height2)
        image2 = np.fromstring(canvas2.tostring_rgb(), dtype='uint8').reshape(height2,width2,3)
        print('IMAGE_______')
        print(image2.shape)
        print(width2)
        print(height2)

        # plt.imshow(image2)
        # plt.show()

        return image.tolist(), height, width, image2.tolist(), height2, width2,