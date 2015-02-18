# K-Nearest Neighbours
Description of method goes here. Imagine you have some training and test data.
\snippet knn.m	 load_data

In order to run KNN, we need to choose a distance, for example Euclidean.
See here for more distances. The distance needs the data we want to classify.
\snippet knn.m choose_distance

Once you have chosen a distance, create an instance of the KNN classifier, passing it training data and labels
\snippet knn.m	 create_instance

Now we run the KNN algorithm and apply it to test data
\snippet knn.m	 train_and_apply
