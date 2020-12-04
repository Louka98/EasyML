# Models and their parameters

## Parameters for the dataset
- "dataset": list of list with sting elements (with size NxM where N is the rows( N, M taken from [1..inf] interval))
- "target_column": a number, indexed from 0 to M-1(M-1 is the last column considering 0 based indexing) example: 3
- "labels_included": true if the data's first row contains the labels for each column false otherwise
- "test_size": example: 0.1 meaning we want 10% of the data to be the testset
## Deep NNs

create_custom'''This function can initialize the models, the parameters are passed as strings from the body of the requests'''
- "model_type":"nn_custom"
- "hidden_act_func": "relu" (or "selu" or "sigmoid" or "softmax" but "relu" is recommended and should be default)
- "act_func": "sigmoid" or "softmax" (or "relu" or "selu" but "sigmoid" or "softmax" is recommended and maybe "sigmoid" should be default)
- "layers": [10,5,3,1]  (meaning we have 4 layers the input layer has 10 neurons and the output layer has 1 neurons (we want to predict 2 different things ) other example [10,5,4] we want to predict 4 different classes)
- "loss":"binary_crossentropy" or "categorical_crossentropy" (default could be "binary_crossentropy")
- "epochs": 10 (meaning we want to have 10 epochs, 10 could be default but could be defined by user and 0 < epochs)
- "batch_size": 10 (10 could be default. it menas we pass 10 examples at the same time to the model this can be any size it could also be a good idea to maximize it as 100 for example, it depends on the performance of our GPU / CPU)
- "early_stopping": True (by default but also can be False)


NEW EXAMPLE: 
{"dataset":[["price","taste","asdf","quality"],["2.0","a","1","good"],["1.0","b","1","good"],["0.0","b","1","bad"],["0.0","c","0","excellent"],["0.0","a","0","bad"],["0.0","a","","sdf"],"",[""]],"target_column":"quality","cat_cols":["taste"],"labels_included":true,"model_type" : "nn_custom","layers" : [10,7,5,3],"act_func": "softmax", "hidden_act_func": "relu", "loss" : "categorical_crossentropy", "batch_size":3, "epochs": 10, "early_stopping":true, "test_size": 0.1}

example for binary classification:
{"dataset":[["100","120","1","1"],["1","0","1","1"],["0","1","1","1"],["0","0","0","0"],["0","1","0","0"]],"target_column":3,"labels_included":false,"model_type" : "nn_custom","layers" : [10,7,5,1],"act_func": "sigmoid", "hidden_act_func": "relu", "loss" : "binary_crossentropy", "batch_size":3, "epochs": 10, "early_stopping":true, "test_size": 0.1 }

example2 for binary classification:
{"dataset":[["price","taste","asdf","quality"],["1","1","1","1"],["1","0","1","1"],["0","1","1","1"],["0","0","0","0"],["0","1","0","0"]],"target_column":3,"labels_included":true,"model_type" : "nn_custom","layers" : [10,7,5,1],"act_func": "sigmoid", "hidden_act_func": "relu", "loss" : "binary_crossentropy", "batch_size":3, "epochs": 10, "early_stopping":true, "test_size": 0.1}

example1 for multi label classification
{"dataset":[["price","taste","asdf","quality"],["1","a","1","good"],["1","b","1","good"],["0","b","1","bad"],["0","c","0","excellent"],["0","a","0","bad"]],"target_column":3,"labels_included":true,"model_type" : "nn_custom","layers" : [10,7,5,3],"act_func": "softmax", "hidden_act_func": "relu", "loss" : "categorical_crossentropy", "batch_size":3, "epochs": 10, "early_stopping":true, "test_size": 0.1}

example2 for binary classification:
{"dataset":[["price","taste","asdf","quality"],["1","1","1","good,excellent"],["1","0","1","good"],["0","1","1","bad,good"],["0","0","0","bad"],["0","1","0","bad"]],"target_column":3,"labels_included":true,"model_type" : "nn_custom","layers" : [10,7,5,3],"act_func": "sigmoid", "hidden_act_func": "relu", "loss" : "binary_crossentropy", "batch_size":3, "epochs": 10, "early_stopping":true, "test_size": 0.1}



result example of a request (will be in the request body):
{
    "acc": [
        0.75,
        0.75,
        0.75
    ],
    "loss": [
        0.5132894515991211,
        0.5090886354446411,
        0.5063337087631226
    ],
    "val_acc": [
        0.0,
        0.0,
        0.0
    ],
    "val_losss": [
        0.7027052044868469,
        0.7039714455604553,
        0.7046418786048889
    ]
}

