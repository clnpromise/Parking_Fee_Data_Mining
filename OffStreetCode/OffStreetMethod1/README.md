### A model to get the off-street parking fee details through picture classfication and Optical Character Recognition.
1. Open pictureUsingAPI.py, you need to change the downloadPath first, then run. All pictures can be downloaded automatically and a file named "paris.txt" is created with directons of each picture.
2. Run classifier.py, the pictures will be classified and transferred into text by calling Baidu APIs, which is stored in "pictureToWords.txt".
3. Run normalization.py, the useful information can be retrieved, which is stored in "pictureDB.txt". Then subtle adjust "pictureDB.txt" manually in case some information is wrong or missed.


