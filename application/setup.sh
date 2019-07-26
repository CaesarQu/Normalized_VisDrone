#!/bin/bash
# Script for installing face recognition pipeline packages and dependencies

sudo apt-get update && sudo apt-get install build-essential
sudo apt-get install cmake
sudo apt install python3-pip
sudo apt-get install unzip

sudo chmod 777 /usr/local/
cd /usr/local

# # Install dlib with python bindings
# git clone https://github.com/davisking/dlib.git
# cd dlib
# mkdir build 
# cd build
# cmake .. 
# cmake --build .
# cd ..
# sudo python3 setup.py install
# cd ..

# # Install face_recognition package for python
# sudo pip3 install face_recognition

# Install OpenCV with python bindings
#sudo pip3 install opencv-python==3.1.0.0
sudo pip3 install opencv-python
sudo rm /var/lib/dpkg/lock
#sudo su
sudo apt update && apt install -y libsm6 libxext6
sudo pip3 install pillow pandas sklearn

# Install and configure tensorflow
sudo pip3 install tensorflow==1.5
sudo apt-get install python-pil python-lxml python3-tk

# Need to install proper protoc compiler version
curl -OL https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip
unzip protoc-3.2.0-linux-x86_64.zip -d protoc3
sudo mv protoc3/bin/* /usr/local/bin/
sudo mv protoc3/include/* /usr/local/include/
sudo ln -s /usr/local/bin/protoc /usr/bin/protoc 

sudo apt-get install python-tk
sudo pip3 install matplotlib
#mkdir face_recog

# Download image dataset from box
sudo wget -O img_dataset.zip https://missouri.box.com/shared/static/3pkpnl2rlcx5lscosqqhqaz89bfssldh.zip
sudo unzip img_dataset
sudo rm img_dataset.zip
cd Face_Recognition_Files
sudo unzip FaceRec_Dataset.zip
sudo rm FaceRec_Dataset.zip
cd lib
sudo wget https://github.com/tensorflow/models/archive/master.zip
sudo unzip master.zip
sudo rm master.zip
sudo cp -r models-master/research api
cd api 
sudo protoc object_detection/protos/*.proto --python_out=.

cd ..
sudo rm -r models-master/
cd ..

echo "Configuration Complete!"

#python pipeline.py