#!/bin/bash
# Script for recording processing times of different image processing functions.

FILES=/usr/local/Face_Recognition_Files/FaceRec_Dataset/lowres/*
# output=/usr/local/"DataOutput.csv"

rm processing_highres.csv
rm processing_lowres.csv

echo -e "File_Name,img_width,img_height,library_loading_time,F1:pre-processing(s),F2:object_detection(s),F3:face_detection(s),F4:face_DB_storage(s),total processing time(s),people_detected,faces_detected" >> processing_highres.csv
startTot=$(date +%s.%N)

for f in $FILES
do
	echo "Processing: $f"
	python3 threadingPipeline.py $f >> output/processing_lowres.csv
done

echo "Transferring complete!"
