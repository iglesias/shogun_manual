# K-Nearest Neighbours
Description of method goes here. Imagine you have some training and test data.
\snippet knn.py	 load_data

In order to run KNN, we need to choose a distance, for example Euclidean.
See here for more distances. The distance needs the data we want to classify.
\snippet knn.py choose_distance

Once you have chosen a distance, create an instance of the KNN classifier, passing it training data and labels
\snippet knn.py	 create_instance

Now we run the KNN algorithm and apply it to test data
\snippet knn.py	 train_and_apply
