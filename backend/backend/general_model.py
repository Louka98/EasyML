from backend.neural_networks import *
import traceback

def init_model(**kwargs):
    '''This function can initialize the models (any model), the parameters are passed as strings from the body of the requests'''
    
    model = None
    try:
        if kwargs['model_type'] == 'nn_custom':

            hidden_act_func = ActivationFunctions[kwargs['hidden_act_func']]
            act_func = ActivationFunctions[kwargs['act_func']]
            model = ClassificationModel(input_shape= kwargs['input_shape'], output_dim= kwargs['layers'][-1], hidden_act_func=ActivationFunctions.relu, act_func=ActivationFunctions.sigmoid)
            model.create_custom(layers= kwargs['layers'], loss = Loss[kwargs['loss']])

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
            
        return hist

    except Exception as e:
        traceback.print_exc()
        
        return None