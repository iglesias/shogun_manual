=====================
K-Nearest-Neighbours
=====================

Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`. Use that for KNN. Blablabla

.. todo:: Update this thing, ss

-------
Example
-------

Imagine you have some training and test data.

.. sgexample:: examples/knn.sg
  :language: python
  :start-after: ![load_data]
  :end-before: ![load_data]

In order to run KNN, we need to choose a distance, for example `Euclidean <http://www.shogun-toolbox.org/doc/en/latest/classshogun_1_1CEuclideanDistance.html>`_.
See `here <http://www.shogun-toolbox.org/doc/en/latest/classshogun_1_1CDistance.html>`_ for more distances. The distance needs the data we want to classify.

.. sgexample:: examples/knn.sg
  :language: python
  :start-after: ![choose_distance]
  :end-before: ![choose_distance]

Once you have chosen a distance, create an instance of the KNN classifier, passing it training data and labels

.. sgexample:: examples/knn.sg
  :language: python
  :start-after: ![create_instance]
  :end-before: ![create_instance]

Now we run the KNN algorithm and apply it to test data

.. sgexample:: examples/knn.sg
  :language: python
  :start-after: ![train_and_apply]
  :end-before: ![train_and_apply]
