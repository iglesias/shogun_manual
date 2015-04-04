=====================
K-Nearest-Neighbours
=====================

Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`. Use that for KNN. Blablabla

-------
Example
-------

Imagine you have some training and test data.

.. sgexample:: ../code/knn.sg:load_data

In order to run KNN, we need to choose a distance, for example CEuclideanDistance, or other sub-classes of CDistance. The distance needs the data we want to classify.

.. sgexample:: ../code/knn.sg:choose_distance

Once you have chosen a distance, create an instance of the CKNN classifier, passing it training data and labels

.. sgexample:: ../code/knn.sg:create_instance

Now we run the KNN algorithm and apply it to test data

.. sgexample:: ../code/knn.sg:train_and_apply
