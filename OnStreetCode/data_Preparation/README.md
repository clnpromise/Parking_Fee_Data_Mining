### Download Street View from Google Place API
1. First go to Google developer page get authentication of Google APIs
2. Modify getLocation.py with your own key, then run. The output is a file named "<city>_Street_Locations", each line represents parameters of one street view picture
3. Change the file name and then run separate.py to separate the output from step 2 into 1000 lines per file if needed. The aim of this step is to prevent IP to be locked by Google
4. Run downloadPic.py to download pictures. Remember to change the input file name. Then the pictures will be stored in file "pictures".

The google street view in Melbourne City and Geelong City is downloaded and classified manually.
All pictures are downloaded by calling Google Street View API
Reference: https://developers.google.com/maps/support/
