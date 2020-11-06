from backend.neural_networks import ActivationFunctions, Loss
from backend.neural_networks import ClassificationModel, ModelTypes
import numpy as np
from tensorflow.keras import layers

def test_binary_classification():
    train_x, train_y = np.vstack((np.random.uniform(low=0., high=10., size=(1000,10)),np.random.uniform(low=11., high=20., size=(1000,10)))), np.hstack((np.ones(1000), np.zeros(1000)))
    model = ClassificationModel(layers= 5, neurons= 20, input_shape= (train_x.shape[-1],))
    model.create_template(type = ModelTypes.binary)
    hist = model.train(train_x,train_y, batch_size=3,val_split=0.2,epochs= 10, early_stopping=False)
    class_ones_res = model.predict(np.random.uniform(low=0., high=10., size=(2,10)))
    class_zeros_res = model.predict(np.random.uniform(low=11., high=20., size=(1,10)))
    assert all(np.around(class_ones_res) == np.ones(class_ones_res.shape))
    assert all(np.around(class_zeros_res) == np.zeros(class_ones_res.shape))

def test_multi_class_classification():
    train_x = np.vstack((np.random.uniform(low=0., high=10., size=(1000,10)),np.random.uniform(low=11., high=20., size=(1000,10)))) 
    
    train_y = np.vstack((np.hstack((np.ones(1000).reshape(1000,1),np.zeros(1000).reshape(1000,1),np.zeros(1000).reshape(1000,1))), np.hstack((np.zeros(1000).reshape(1000,1),np.ones(1000).reshape(1000,1),np.zeros(1000).reshape(1000,1)))))

    model = ClassificationModel(layers= 10, neurons= 20, input_shape= (train_x.shape[-1],), output_dim=train_y.shape[-1])
    model.create_template(type = ModelTypes.multi_class)
    hist = model.train(train_x,train_y, batch_size=3,val_split=0.2,epochs= 10, early_stopping=False)
    assert (np.around(model.predict(np.random.uniform(low=0., high=10., size=(1,10)))) == np.array([1., 0., 0.])).all()
    assert (np.around(model.predict(np.random.uniform(low=11., high=20., size=(1,10)))) == np.array([0., 1., 0.])).all()

def test_multi_label_classification():
    train_x = np.vstack((np.random.uniform(low=0., high=10., size=(1000,10)),np.random.uniform(low=11., high=20., size=(1000,10)))) 
    
    train_y = np.vstack((np.hstack((np.ones(1000).reshape(1000,1),np.zeros(1000).reshape(1000,1),np.ones(1000).reshape(1000,1))), np.hstack((np.zeros(1000).reshape(1000,1),np.ones(1000).reshape(1000,1),np.zeros(1000).reshape(1000,1)))))

    model = ClassificationModel(layers= 10, neurons= 20, input_shape= (train_x.shape[-1],), output_dim=train_y.shape[-1])
    model.create_template(type = ModelTypes.multi_label)
    hist = model.train(train_x,train_y, batch_size=3,val_split=0.2,epochs= 10, early_stopping=False)
    assert (np.around(model.predict(np.random.uniform(low=0., high=10., size=(1,10)))) == np.array([1., 0., 1.])).all()
    assert (np.around(model.predict(np.random.uniform(low=11., high=20., size=(1,10)))) == np.array([0., 1., 0.])).all()

def test_create_custom_as_binary_classification():
    train_x, train_y = np.vstack((np.random.uniform(low=0., high=10., size=(1000,10)),np.random.uniform(low=11., high=20., size=(1000,10)))), np.hstack((np.ones(1000), np.zeros(1000)))
    
    model = ClassificationModel(input_shape= (train_x.shape[-1],), output_dim= 1, hidden_act_func=ActivationFunctions.relu, act_func=ActivationFunctions.sigmoid)

    layers = [10,7,5,1]
    model.create_custom(layers= layers, loss = Loss.binary_crossentropy)

    hist = model.train(train_x,train_y, batch_size=3,val_split=0.2,epochs= 10, early_stopping=False)
    class_ones_res = model.predict(np.random.uniform(low=0., high=10., size=(2,10)))
    class_zeros_res = model.predict(np.random.uniform(low=11., high=20., size=(1,10)))
    assert all(np.around(class_ones_res) == np.ones(class_ones_res.shape))
    assert all(np.around(class_zeros_res) == np.zeros(class_ones_res.shape))