$(document).ready(function () {

    $("#algorithm").change(function () {
        switch ($('#algorithm').val()) {
            case "KM":
                $("#textalgo").remove();
                $("#imgAlgo").remove();
                $("<div class=\"row doc docText\" id='textalgo'>" +
                    "This algorithm is one of the simplest and popular unsupervised machine learning algorithms.</br>" +
                    "You’ll define a target number </br>" +
                    "k: which refers to the number of centroids you need in the dataset. </br>" +
                    "A centroid : the imaginary or real location representing the center of the cluster.</br>" +
                    "Every data point is allocated to each of the clusters through reducing the in-cluster sum of squares.</br>" +
                    "In other words\, the K-means algorithm identifies k number of centroids\, and then allocates every data" +
                    "   point to the nearest cluster, while keeping the centroids as small as possible.</br>" +
                    "   The ‘means’ in the K-means refers to averaging of the data; that is, finding the centroid.</br>" +
                    "   To process the learning data, the K-means algorithm in data mining starts with a first" +
                    "   group of randomly selected centroids, which are used as the beginning points for every cluster, and then performs" +
                    "   iterative (repetitive) calculations to optimize the positions of the centroids</br>" +
                    "   It halts creating and optimizing clusters when either: The centroids have stabilized —" +
                    "   there is no change in their values because the clustering has been successful.</br>" +
                    "   The defined number of iterations has been achieved. </br> </br>" +
                    "   <h5> Picture :</h5> </p>" +
                    "  <ul>" +
                    "   <li>Figure 1 shows the representation of data of two different items. the first item has shown in blue color and the second item has shown in red color. Here I am choosing the value of K randomly as 2." +
                    "   There are different methods by which we can choose the right k values." +
                    "   </li>" +
                    "   <li>In figure 2, Join the two selected points. Now to find out centroid, we will" +
                    "   draw a perpendicular line to that line. The points will move to their centroid. If you will notice there, then you" +
                    "  will see that some of the red points are now moved to the blue points. Now, these" +
                    "   points belong to the  group of blue color items." +
                    "   </li>" +
                    "   <li>The same process will continue in figure 3. we will join the two points and draw" +
                    "   a perpendicular line to that and find out the centroid. Now the two points will move to its" +
                    "   centroid and again some of the red points get converted to blue points." +
                    "   </li>" +
                    "   <li>The same process is happening in figure 4. This process will be continued until" +
                    "   and unless we  get two completely different clusters of these groups." +
                    "   </li>" +
                    "   </ul>" +
                    "   </br>" +
                    "   <h5> Video :</h5>" +
                    "   <iframe class=\"video\" src=\"https://www.youtube.com/embed/4b5d3muPQmA\" frameborder=\"0\"" +
                    "allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"" +
                    "allowfullscreen></iframe>" +
                    "</iframe>" +
                    "</br>source : <a  href=\"https://en.wikipedia.org/wiki/DBSCAN\">Link</a></br>"+
                    "</div>"
                ).insertAfter("#algoInput");
                $("<div class=\"col-md-6 col-sm-12 col-lg-6 vertical-center ImgDoc doc\" id=\"imgAlgo\">\n" +
                    "     <img src=\"https://editor.analyticsvidhya.com/uploads/34513k%20means.png\" width=\"100%\">\n" +
                    "        </div>").insertAfter("#firstCol");

                break;
            case "AC":
                $("#textalgo").remove();
                $("#imgAlgo").remove();
                $("<div class=\"row doc docText\" id='textalgo'>" +
                    "uses a bottom-up approach, where in each data point starts in its own cluster. These clusters are then joined greedily, by taking the two most similar clusters together and merging them.\n" +
                    "Different metrics can be used for distance between two points: Euclidean distance, Manhattan distance, Max distance and others\n" +
                    "Linkage criteria:\n" +
                    "Ward minimizes the variance of the clusters being merged.\n" +
                    "Average uses the average of the distances of each observation of the two sets.\n" +
                    "Complete or maximum linkage uses the maximum distances between all observations of the two sets.\n" +
                    "Single uses the minimum of the distances between all observations of the two sets.\n" +
                    "<h5> Video :</h5>" +
                    "<iframe class=\"video\" src=\"https://www.youtube.com/embed/7xHsRkOdVwo\" frameborder=\"0\"" +
                    "allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"" +
                    "allowfullscreen></iframe>" +
                    "</br>source : <a  href=\"https://towardsdatascience.com/hierarchical-clustering-and-its-applications-41c1ad4441a6\">Link</a></br>"
                ).insertAfter("#algoInput");
                $("<div class=\"col-md-6 col-sm-12 col-lg-6 vertical-center ImgDoc \" id=\"imgAlgo\">\n" +
                    "     <img src=\"Images/AC.png\" width=\"90%\">\n" +
                    "        </div>").insertAfter("#firstCol");
                break;
            case "DBSCAN":
                $("#textalgo").remove();
                $("#imgAlgo").remove();
                $("<div class=\"row doc docText\" id='textalgo'>" +
                    "DBSCAN requires two parameters:" +
                    "ε (eps) and the minimum number of points required to form a dense region (minPts)." +
                    "It starts with an arbitrary starting point that has not been visited." +
                    "This point\'s ε-neighborhood is retrieved, and if it contains sufficiently many points, a cluster is started. Otherwise, the point " +
                    "is labeled as noise. Note that this point might later be found in a sufficiently sized ε-environment of a different point and hence be made part of a cluster.</br>" +
                    "If a point is found to be a dense part of a cluster, its ε-neighborhood is also part of that cluster. Hence, all points that are found within the ε-neighborhood " +
                    "are added, as is their own ε-neighborhood when they are also dense. This process continues until the density-connected cluster is completely found. Then, a new" +
                    "unvisited point is retrieved and processed, leading to the discovery of a further cluster or noise.</br>" +
                    "DBSCAN can be used with any distance function (as well as similarity functions or other predicates)." +
                    "The distance function (dist) can therefore be seen as an additional parameter.</br></br>" +
                    "Example:</br>" +
                    "In this diagram, minPts = 4. Point A and the other red points are core points, because the area surrounding these" +
                    "points in an ε radius contain at least 4 points (including the point itself). Because they are all reachable from one another, " +
                    "they form a single cluster. Points B and C are not core points, but are reachable from A (via other core points) and thus belong to the" +
                    "cluster as well. Point N is a noise point that is neither a core point nor directly-reachable.</br>" +
                    "<h5> Video :</h5>" +
                    "<iframe class=\"video\" src=\"https://www.youtube.com/embed/C3r7tGRe2eI\" frameborder=\"0\"" +
                    "allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"" +
                    "allowfullscreen></iframe>" +
                    "</br>source : <a  href=\"https://en.wikipedia.org/wiki/DBSCAN\">Link</a></br>"
                ).insertAfter("#algoInput");
                $("<div class=\"col-md-6 col-sm-12 col-lg-6 vertical-center ImgDoc \" id=\"imgAlgo\">\n" +
                    "     <img src=\"Images/DBSCAN.png\" width=\"90%\">\n" +
                    "        </div>").insertAfter("#firstCol");
                break;
            case "EM":
                $("#textalgo").remove();
                $("#imgAlgo").remove();
                $("<div class=\"row doc docText\" id='textalgo'>"+"The elbow method is a heuristic used in determining the number of clusters in a data set. The method consists of plotting the explained variation as a function of the number of clusters, and picking the elbow of the curve as the number of clusters to use. The same method can be used to choose the number. \n" +
                    "\n" +
                    "The main idea behind elbow method is, when adding more clusters doesn’t improve the performance of model. WCSS (within clusters sum of squares) is calculating for each clusters in defined range and graph plotted. The value of WCSS decrease rapidly until it reaches the ideal number of k and after that point is start decreasing slowly. This graph look like elbow and where “elbow” occurs is ideal number of k. \n" +
                    "\n" +
                    "Silhouette scor This is a better measure to decide the number of clusters to be formulated from the data. It is calculated for each instance and the formula goes like this:\n" +
                    "\n" +
                    " \n" +
                    "\n" +
                    "Silhouette Coefficient = (x-y)/ max(x,y)\n" +
                    "\n" +
                    "where, y is the mean intra cluster distance: mean distance to the other instances in the same cluster. x depicts mean nearest cluster distance i.e. mean distance to the instances of the next closest cluster.\n" +
                    "\n" +
                    "The coefficient varies between -1 and 1. A value close to 1 implies that the instance is close to its cluster is a part of the right cluster. Whereas, a value close to -1 means that the value is assigned to the wrong cluster.\n" +
                    "\n " +
                    "As per this method k=3 was a local optima, whereas k=5 should be chosen for the number of clusters. This method is better as it makes the decision regarding the optimal number of clusters more meaningful and clear. But this metric is computation expensive as the coefficient is calculated for every instance. Therefore, decision regarding the optimal metric to be chosen for the number of cluster decision is to be made according to the needs of the product."
                    +"<h5> Video :</h5>" +
                    "<iframe class=\"video\" src=\"https://www.youtube.com/embed/qs8nfzUsW5U\" frameborder=\"0\"" +
                    "allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"" +
                    "allowfullscreen></iframe>" +
                    "</br>source : <a  href=\"                https://medium.com/@jyotiyadav99111/selecting-optimal-number-of-clusters-in-kmeans-algorithm-silhouette-score-c0d9ebb11308\n\">Link</a></br>"





                ).insertAfter("#algoInput");
                $("<div class=\"col-md-6 col-sm-12 col-lg-6 vertical-center ImgDoc \" id=\"imgAlgo\">\n" +
                    "     <img src=\"Images/EM.png\" width=\"65%\">\n" +
                    "        </div>").insertAfter("#firstCol");
                break;
            case "MSC":
                $("#textalgo").remove();
                $("#imgAlgo").remove();
                $("<div class=\"row doc docText\" id='textalgo'>"+
                    "Meanshift is falling under the category of a clustering algorithm in contrast of Unsupervised learning that assigns the data points to the clusters iteratively by shifting points towards the mode (mode is the highest density of data points in the region, in the context of the Meanshift). As such, it is also known as the Mode-seeking algorithm. Mean-shift algorithm has applications in the field of image processing and computer vision.\n" +
                    "\n" +
                    "Given a set of data points, the algorithm iteratively assigns each data point towards the closest cluster centroid and direction to the closest cluster centroid is determined by where most of the points nearby are at. So each iteration each data point will move closer to where the most points are at, which is or will lead to the cluster center. When the algorithm stops, each point is assigned to a cluster. </br>"+
                    "<h5> Video :</h5>" +
                    "<iframe class=\"video\" src=\"https://www.youtube.com/embed/3ERPpzrDkVg\" frameborder=\"0\"" +
                    "allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"" +
                    "allowfullscreen></iframe>" +
                    "</br>source : <a  href=\"https://www.geeksforgeeks.org/ml-mean-shift-clustering/ \">Link</a></br>"
                ).insertAfter("#algoInput");
                $("<div class=\"col-md-6 col-sm-12 col-lg-6 vertical-center ImgDoc \" id=\"imgAlgo\">\n" +
                    "     <img src=\"https://media.geeksforgeeks.org/wp-content/uploads/20190508162515/anigif.gif\" width=\"80%\">\n" +
                    "        </div>").insertAfter("#firstCol");
                break;

            case "N":
                $("#textalgo").remove();
                $("#imgAlgo").remove();
                $("<div class=\"row doc docText\" id='textalgo'>"+
                    ""+
                     +"<h5> Video :</h5>" +
                    "<iframe class=\"video\" src=\"https://www.youtube.com/embed/qs8nfzUsW5U\" frameborder=\"0\"" +
                    "allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"" +
                    "allowfullscreen></iframe>" +
                    "</br></br>"
                ).insertAfter("#algoInput");
                $("<div class=\"col-md-6 col-sm-12 col-lg-6 vertical-center ImgDoc \" id=\"imgAlgo\">\n" +
                    "     <img src=\"Images/DBSCAN.png\" width=\"90%\">\n" +
                    "        </div>").insertAfter("#firstCol");
                break;
            case "SC":
                $("#textalgo").remove();
                $("#imgAlgo").remove();
                $("<div class=\"row doc docText\" id='textalgo'>"+
                    "Spectral clustering has become increasingly popular due to its simple implementation and promising performance in many graph-based clustering. It can be solved efficiently by standard linear algebra software, and very often outperforms traditional algorithms such as the k-means algorithm.\n" +
                    "\n" +
                    "To perform a spectral clustering 3 main steps are needed:\n" +
                    "\n" +
                    "1. Create a similarity graph between our N objects to cluster.\n" +
                    "\n" +
                    "2. Compute the first k eigenvectors of its Laplacian matrix to define a feature vector for each object.\n" +
                    "\n" +
                    "3. Run k-means on these features to separate objects into k classes.\n" +
                    "\n" +
                    "Ways to construct graph:\n" +
                    "\n" +
                    "ε-neighborhood graph: Each vertex is connected to vertices falling inside a ball of radius ε where ε is a real value that has to be tuned in order to catch the local structure of data.\n" +
                    "\n" +
                    "k-nearest neighbor graph: Each vertex is connected to its k-nearest neighbors where k is an integer number which controls the local relationships of data."+
                    +"<h5> Video :</h5>" +
                    "<iframe class=\"video\" src=\"https://www.youtube.com/embed/uxsDKhZHDcc\" frameborder=\"0\"" +
                    "allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"" +
                    "allowfullscreen></iframe>" +
                    "</br>source : <a  href=\"https://towardsdatascience.com/spectral-clustering-for-beginners-d08b7d25b4d8 \">Link</a></br>"
                ).insertAfter("#algoInput");
                $("<div class=\"col-md-6 col-sm-12 col-lg-6 vertical-center ImgDoc \" id=\"imgAlgo\">\n" +
                    "     <img src=\"Images/SC.PNG\" width=\"90%\">\n" +
                    "        </div>").insertAfter("#firstCol");
                break;
            case "S":
                $("#textalgo").remove();
                $("#imgAlgo").remove();
                $("<div class=\"row doc docText\" id='textalgo'>"+
                    "<p>In machine learning, we can handle various types of data, e.g. audio signals and pixel values for image data, and this data can include multiple dimensions. Feature standardization makes the values of each feature in the data have zero-mean (when subtracting the mean in the numerator) and unit-variance. This method is widely used for normalization in many machine learning algorithms (e.g., support vector machines, logistic regression, and artificial neural networks).[2][citation needed] The general method of calculation is to determine the distribution mean and standard deviation for each feature. Next we subtract the mean from each feature. Then we divide the values (mean is already subtracted) of each feature by its standard deviation.\n" +
                    "Standardizing the features around the center and 0 with a standard deviation of 1 is important when we compare measurements that have different units. Variables that are measured at different scales do not contribute equally to the analysis and might end up creating a bais.\n" +
                   "For example, A variable that ranges between 0 and 1000 will outweigh a variable that ranges between 0 and 1. Using these variables without standardization will give the variable with the larger range weight of 1000 in the analysis. Transforming the data to comparable scales can prevent this problem. Typical data standardization procedures equalize the range and/or data variability.\n" +
                    "</p><img class='docTextImg imgN' src=\"Images/E1.png\"> <br>" +
                    "<p>Where x is the original feature vector,</p>" +
                    "<img class='docTextImg imgN' src=\"Images/E2.png\"><br>" +
                    " <p>is the mean of that feature vector, and &sigma; is its standard deviation." +
                    "Standardization assumes that your data has a Gaussian (bell curve) distribution. This does not strictly have to be true, but the technique is more effective if your attribute distribution is Gaussian. Standardization is useful when your data has varying scales and the algorithm you are using does make assumptions about your data having a Gaussian distribution, such as linear regression, logistic regression, and linear discriminant analysis.</p> <br>"+
                    +"<h5>Video :</h5>" +
                    "<iframe class=\"video\" src=\"https://www.youtube.com/embed/qs8nfzUsW5U\" frameborder=\"0\"" +
                    "allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\"" +
                    "allowfullscreen></iframe>" +
                    "</br>source : <a  href=\"https://towardsai.net/p/data-science/how-when-and-why-should-you-normalize-standardize-rescale-your-data-3f083def38ff \"></a></br>"
                ).insertAfter("#algoInput");
                $("<div class=\"col-md-6 col-sm-12 col-lg-6 vertical-center ImgDoc \" id=\"imgAlgo\">\n" +
                    "     <img src=\"Images/DBSCAN.png\" width=\"90%\">\n" +
                    "        </div>").insertAfter("#firstCol");
                break;

            case "DNN":
                $("#textalgo").remove();
                $("#imgAlgo").remove();
                $("<div class=\"row doc docText\" id='textalgo'>"+
                    "Here you can choose between different pre-defined deep learning classification \n" +
                    "models or you can build your own. These models are great when:" +
                    "<ul>" +
                    "<ul>" +
                    "<li>you have labels for your data.</li>" +
                    "<li> the dataset is large.</li>" +
                    "</ul>" +
                    "<b>Disadvantages:</b>" +
                    "<ul>" +
                    "<li> if you have a small dataset a normal supervised learning algorithm is much better.</li>" +
                    "<li> the training can take some time.</li>" +
                    "</ul>" +

                    "</ul>" +

                    "<h4 class='blueTextHero'>Model types:</h4>" +

                    "<ul>" +

                    "<b>Binary classification:</b>" +
                    "<ul>" +
                    "<li> use this when you want to categories your data into two categories<br>" +
                    "</ul>" +

                    "<b>Multi class classification:</b>" +
                    "<ul>" +
                    "<li> these models should be used when you have multiple classes and one instance can only belong in one class (it can have only one label).</li>" +
                    "</ul>" +

                    "<b>Multi label:</b>" +
                    "<ul>" +
                    "<li> when you want to assign multiple classes to an instance</li>" +
                    "</ul>" +

                    "</ul>" +


                    "<h4 class='blueTextHero'>Model layer architecture:</h4>" +
                    "Adding more layers to you neural network can be very useful. If you add layers you increase the number of learnable parameters which can lead to a greater feature recognition ability. \n" +
                    "Pay attention to:" +
                    "<ul>" +
                    "<ul>" +
                    "<li> The <b>number of neurons in the last layer</b>. It will determine the number of classes your network can predict. It should<b>always equal to the number of different labels</b> you have in your dataset. </li>\n" +
                    "<li> The <b>more layers and neurons</b> you use the <b>greater the training time</b> will take  </li>\n" +
                    "</ul>" +
                    "</ul>" +
                    "<h5> Activation functions:</h5>" +
                    "\tThe activation function you can use for the last layer of the neural network or in the hidden layers.\n" +
                    "<h4 class='blueTextHero'>Sigmoid:</h4>\n" +
                    "<p>Use this for binary or multi label models.</p>" +

                    "<img class='docTextImg imgDNN'  src=\"Images/Sigmoid.png\">" +
                    "<p>The function squashes the input between 0 and 1 so we can get probabilities for both our classes.</p>" +

                    "<h4 class='blueTextHero'>Softmax</h4>\n" +
                    "<p>Use this function for multi class classification.</p>" +
                    "<img class='docTextImg '  src=\"Images/softmax.PNG\" width='40%'>" +
                    "<p>This function gives us a probability distribution with as many different probabilities as the numbers of neurons in the output layer. The sum of these probabilities equal to 1 and all the values are in the (0,1) interval.</p>" +
                    "<h4 class='blueTextHero'>Relu:</h4>" +
                    "<p>This function usually used as activation function for the hidden layers. It is a great function because it solves the problem of vanishing gradients.</p>" +

                    "<img class='docTextImg imgDNN'  src=\"Images/relu.PNG\">" +

                    "<h4 class='blueTextHero'>Selu</h4>\n" +
                    "<p>Similar to the relu function, for x > 0 they are the same but below that it does not produces 0.</p>" +
                    "<img class='docTextImg imgDNN'  src=\"Images/selu.png\" width='60%'>" +

                    "<h4 class='blueTextHero'> Loss functions:</h4>" +
                    "Loss functions are used to measure our models performance. This will be also utilized when we update the weights of our models, so it's important to choose them correctly. \n" +
                    "Updating our weights will be based on the gradient of the loss function. The gradient shows us which direction does the loss grows the most. We can utilize this by taking the opposite direction of it as that will show us the steepest decrease in the loss. If we know which direction our loss decreases, we can just update the weights of our model based on it. \n" +
                    "<h4 class='blueTextHero'> Binary crossentropy:</h4>" +
                    "Use it in the case of:" +
                    "<ul>" +
                    "<ul>" +
                    "<li>binary classification </li>\n" +
                    "<li>multi label classification </li>\n" +
                    "</ul>" +
                    "</ul>" +
                    "<img class='docTextImg'  src=\"Images/BCE.png\" width='75%'>" +


                    "<ul>" +
                    "<ul>" +
                    "<li><font face=\"Symbol\">q</font> denotes all the weights </li>" +
                    "<li>N is the number of examples </li>" +
                    "<li>y<sub>i</sub>-s are the true labels, can be either 0 or 1</li>" +
                    "<li>y<sub>i</sub>  are from the [0,1] interval, these are the labels predicted by our model.</li>" +
                    "</ul>" +
                    "</ul>" +

                     "<p>The lower the loss the better.To understand this, we first take a look at the log(x) function:</p>" +
                    "<!--<img class='docTextImg imgDNN'  src=\"https://editor.analyticsvidhya.com/uploads/34513k%20means.png\" \">-->" +

                    "<p>We can see that the closer we are to zero the greater the value of the -log(x) and if we are close to one the value is really small. In the case of one the -log(1) = 0.</p>" +

                    "<p>Now going back to J(<font face=\"Symbol\">q</font>) equation. <br>If our model had a 100% accuracy our total loss would be 0. <br>If we predict 1and the true label would be also 1 we would end up with the following :<br> 1 ∗ log(1) + (1− 1) ∗ log(1−1) = 1 * 0+ 0 * log(0) = 0.<br></p>"+


                    "<p> The case of predicting 0 and the true label being 0 is almost the same and we would also end up with zero. Between these values we just penalize our model based on \"how far\" its guess is from the real label.\n</p>"+


                    "<h4 class='blueTextHero'> Categorical crossentropy:</h4>\n" +
                    "Use it in the case of:" +
                    "- multi class classification (always use it with the softmax activation function)" +
                    "<img class='docTextImg imgDNN'  src=\"Images/ce_loss.png\" width='60%'>" +
                    "<ul>" +
                    "<li> N is the number of examples </li>" +
                    "<li> M the number of possible classes (= the number of neurons in the last layer) </li>" +
                    "<li> y<sub>i</sub> is the one-hot encoded representation of the label </li>" +
                    "<li> y<sup>i</sup> is the predicted \"one-hot\" vector </li>" +
                    "</ul>" +
                    "<h4 class='blueTextHero'>Target column:</h4>" +
                    "The exact name of the target column, what you want to use as labels for you data." +
                    "<h4 class='blueTextHero'>Categorical column:</h4>" +
                    "The names of the categorical columns separated with comma and no spaces needed." +
                    "<h4 class='blueTextHero'>Epochs:</h4>" +
                    "The number of epochs you want to train the network." +
                    "In each epoch the network will see all the data from the dataset." +
                    "We use early stopping so if the training does not improve after a few epochs we simply stop training the model." +
                    "<h4 class='blueTextHero'>Test size:</h4>" +
                    "The size of the test dataset. If set to 0,1 the data will be split the following way: 90% of the data for training and 10% of it for testing.<br>"
                ).insertAfter("#algoInput");
                $("<div class=\"col-md-6 col-sm-12 col-lg-6 vertical-center ImgDoc \" id=\"imgAlgo\">\n" +
                    "     <img src=\"Images/dnn.png\" width=\"90%\">\n" +
                    "        </div>").insertAfter("#firstCol");
                break;
            default:
                alert('error');
                break;
        }
    });

});

