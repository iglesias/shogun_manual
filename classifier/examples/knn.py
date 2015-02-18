from modshogun import EuclideanDistance, KNN, MulticlassLabels, CSVFile, RealFeatures

#! [load_data]
trainf = CSVFile("../data/fm_train_real.dat")
feats_train = RealFeatures(trainf)
testf = CSVFile("../data/fm_test_real.dat")
feats_test = RealFeatures(testf)
train_labels = CSVFile("../data/label_train_multiclass.dat")
labels = MulticlassLabels(train_labels)
#! [load_data]

#! [choose_distance]
distance = EuclideanDistance(feats_train, feats_test)
#! [choose_distance]

#! [create_instance]
knn = KNN(3, distance, labels)
#! [create_instance]

#! [train_and_apply]
knn.train()
test_labels = knn.apply(feats_test)
output = test_labels.get_values()
print output
#! [train_and_apply]

