# Models and their parameters

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

{"dataset":[["100","120","1","1"],["1","0","1","1"],["0","1","1","1"],["0","0","0","0"],["0","1","0","0"]],"target_column":3,"labels_included":false,"model_type" : "nn_custom","layers" : [10,7,5,1],"act_func": "sigmoid", "hidden_act_func": "relu", "loss" : "binary_crossentropy", "batch_size":3, "epochs": 10, "early_stopping":true, "test_size": 0.1 }

example2: {"dataset":[["price","taste","asdf","quality"],["1","1","1","1"],["1","0","1","1"],["0","1","1","1"],["0","0","0","0"],["0","1","0","0"]],"target_column":3,"labels_included":true,"model_type" : "nn_custom","layers" : [10,7,5,1],"act_func": "sigmoid", "hidden_act_func": "relu", "loss" : "binary_crossentropy", "batch_size":3, "epochs": 10, "early_stopping":true, "test_size": 0.1}