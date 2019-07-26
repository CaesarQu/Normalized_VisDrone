# REU_offloading
This is the main repository for REU application on drone offloading and more

## application 
Application Folder consists of the analytics platform, transmission and processing bash scripts, setup script for correct testing enviornment, and graphs of our results

AnalyticsPlatform.py consists of four Machine Learning models to predict processing and transmission times on the various models. To run the code, type "python3 AnalyticsPlatform.py [transmission/processing] [your .csv file]" in your terminal. Make sure to midfy in the code the name of your .csv file and where it was located.

TxExp.sh was used to find the transmission times of our data

processingTime.sh was used to find the processing times of our data. It uses the threadingPipeline.py file found in the "algorithm" folder.

setup.sh installs the necessary packages in order to successfully test our data.

The graphs folder contains matlab code of the graphs of our results.
## algorithm
Algorithm folder shows the pro-existing algorithms we condsider to compare with our offloading algorithm.

The job-shop-scheduling folder contains two files. One of the files contains our approach in calculating optimal scheduling time. The other file calculates optimal scheduling time for a random offloading approach.

The threadingPipeline folder contains files that have an object detection application pretrained to detect pedestrians. One of the files is a decomposed version of the application where the four functions can be ran separately.

## dataset
Dataset folder consists data and log files generate by application.

The processing_data folder contains processing data of livestreams that are sparely or densely populated with pedestrians. The livestreams were processed on various virtual machines.

The transmission_data folder contains the results of transmitting live-streams from a laptop to the NVidia Jetson Nano.

The txBand folder contains the results of transmitting live-streams from a Desktop to a NVidia Jetson Nano at different network speeds (10, 5, 2, and 1 mbps).

TxExp1_Master.csv is the master file in which it contains all of our transmission bandwidth data that was collected from transmitting the livestreams from a desktop to the NVidia Jetson Nano.

total_processing.csv is the master file in which it processed as many images as it could on the NVidia Jetson Nano before the power life of a power bank ran out of power since the Jetson's power source was connected to a 10,000 mAh power bank. 

The jobshopdata.xlsx contains the optimal scheduling time and average energy consumption per drone of four offloading schemes: offload only, local only, random offloading, and our approach.

## Author
Chengyi Qu, Jeromy Yu, Aditya Vandanapu
## Date start
July 26, 2019
