import org.shogun.*;
import org.jblas.*;

class knn {
    static {
        System.loadLibrary("modshogun");
    }

    public static void main(String argv[]) {
        modshogun.init_shogun_with_defaults();

        //![begin]
        //![load_data]
        CSVFile trainf = new CSVFile("../data/fm_train_real.dat");
        RealFeatures feats_train = new RealFeatures(trainf);
        CSVFile testf = new CSVFile("../data/fm_test_real.dat");
        RealFeatures feats_test = new RealFeatures(testf);
        CSVFile train_labels = new CSVFile("../data/label_train_multiclass.dat");
        MulticlassLabels labels = new MulticlassLabels(train_labels);
        //![load_data]

        //![choose_distance]
        EuclideanDistance distance = new EuclideanDistance(feats_train, feats_test);
        //![choose_distance]

        //![create_instance]
        KNN knn = new KNN(3, distance, labels);
        //![create_instance]

        //![train_and_apply]
        knn.train();
        Labels test_labels = knn.apply(feats_test);
        DoubleMatrix output = test_labels.get_values();
        System.out.println(output);
        //![train_and_apply]
        //![end]

    }
}
