### On-Street Parking Panel Recognition
1. "OpenCV Classifier" file contains positive and negative samples and the detailed classifier is stored in "data". If you want to train your own classifier:

   1. Prepare negative backgrounds stored in "neg" and neg.txt explains the direction of each pictures

   2. Prepare target samples and store them in file "sample"

   3. Run "createPositiveSamples.py" (change the parameters if needed), the positive samples will be created automatically

   4. In terminal, go to the classifier direction, train the classifier (change the parameters if needed), then the trained result will be stored in file "data"

      "opencv_traincascade -data data -vec pos.vec -bg neg.txt -numPos 8000 -numNeg 8000 -numStages 15 -w 20 -h 30"

2. Prepare the dataset, modify directions in "openCVRecognize.py", then run "openCVRecognize.py" to classify the street view

3. "CNNs" file contains the jupyter notebook to implement CNNs. Tensorflow should be installed first.

   1. "augmentation.ipynb": used to create more positive samples by using Keras

   2. The other 3 notebook are in similar structure:

      i. "Prj_CNN_1.ipynb": used initially to classify the whole street view

      ii. "ParkingSignClassifier.ipynb": used to train Melbourne City parking panels with output from OpenCV

      iii. "ParkingSIgnClassifier_Geelong.ipynb": used in Geelong city application 

   3. TensorFlowTrain including pictures for training



All example pictures are downloaded by calling Google Street View API
Reference: https://developers.google.com/maps/support/