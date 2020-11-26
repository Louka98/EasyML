from backend.neural_networks import *
from algorithms.Clusters import clustering
import traceback

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
                n_clusters = model.nclusters(kwargs['dataset'])                
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