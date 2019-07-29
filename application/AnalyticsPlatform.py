# Analytics Sandbox for evaluating various machine learning models on KDN data
# Author: Jon Patman | 2017
# Additonal Modifications: Aditya Vandanapu

from __future__ import division
import time
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
from sklearn.kernel_ridge import KernelRidge
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.svm import LinearSVR
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import LeaveOneOut
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import Imputer
from sklearn import linear_model

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split

def kFoldsCrossValidation(modelName,model,X,y, y_pred):
    print(modelName, "scores:")
    scores = cross_val_score(model, X, y, scoring="neg_mean_absolute_error", cv=10)
    print('MAE =', -scores.mean())
    rmse_scores = mean_squared_error(y,y_pred)
    print('RMSE =', math.sqrt(rmse_scores))

def loadData(fileName,features,target):
    X = pd.DataFrame(pd.read_csv(fileName), columns=features)
    y = pd.DataFrame(pd.read_csv(fileName), columns=target)
    y = y['Transfer Time (Hours)']
    return X,y


expType = sys.argv[1]

# Transmission dataset is used
if expType == 'transmission':
    inputFeatures = pd.DataFrame(pd.read_csv('data/TxExp1_Master.csv'), columns=['Transmission_BW (kbps)','ImgHeight','ImgWidth', 'Datasize','Datasize (bits)','Tx_calc'])
    targetFeatures = pd.DataFrame(pd.read_csv('data/TxExp1_Master.csv'), columns=['Tx_true'])
    X = inputFeatures
    y = targetFeatures['Tx_true']
    print('\nBenchmarking ML models on the',expType,'dataset...\n')
# Processing dataset is used
elif expType == 'processing':
    inputFeatures = pd.DataFrame(pd.read_csv('data/total_processing.csv'), columns=['imgWidth','imgHeight', 'library_loading_time', 'F1:pre-processing(s)', 'F2:object_detection(s)', 'F3:face_detection(s)', 'F4:face_DB_storage(s)', 'people_detected', 'faces_detected'])
    targetFeatures = pd.DataFrame(pd.read_csv('data/total_processing.csv'), columns=['T_p'])
    X = inputFeatures
    y = targetFeatures['T_p']
    print('\nBenchmarking ML models on the', expType, 'dataset...\n')
else:
    print ('Please enter a valid dataset (experiment) name.')
    exit()

ridReg = linear_model.Ridge(alpha=0.005)
t0_train = time.time()
ridReg.fit(X,y)
t1_train = time.time()
t0_pred = time.time()
y_pred = ridReg.predict(X)
t1_pred = time.time()
y_ridReg = ridReg.predict(X)
kFoldsCrossValidation('Kernel-Ridge Regression',ridReg,X,y, y_ridReg)
print("training time: %.12f" % (t1_train - t0_train))
print("prediction latency: %.12f\n" % (t1_pred - t0_pred))

# Support Vector Regression model
svr_rbf = SVR(kernel='rbf', gamma=0.1, C=100.0)
t0_train = time.time()
svr_rbf.fit(X,y)
t1_train = time.time()
t0_pred = time.time()
y_svr = svr_rbf.predict(X)
t1_pred = time.time()
kFoldsCrossValidation('SVR-RBF',svr_rbf,X,y, y_svr)
print("training time: %.12f" % (t1_train - t0_train))
print("prediction latency: %.12f\n" % (t1_pred - t0_pred))

# Gaussian Process model
kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
t0_train = time.time()
gp.fit(X,y)
t1_train = time.time()
t0_pred = time.time()
y_gp = gp.predict(X)
t1_pred = time.time()
kFoldsCrossValidation('Gaussian Process Regression',gp,X,y,y_gp)
print("training time: %.12f" % (t1_train - t0_train))
print("prediction latency: %.12f\n" % (t1_pred - t0_pred))

rfReg = RandomForestRegressor(random_state=2, n_estimators=100)
t0_train = time.time()
rfReg.fit(X,y)
t1_train = time.time()
t0_pred = time.time()
y_rfReg = rfReg.predict(X)
t1_pred = time.time()
kFoldsCrossValidation('Random Forest Regression',rfReg,X,y,y_rfReg)
print("training time: %.12f" % (t1_train - t0_train))
print("prediction latency: %.12f\n" % (t1_pred - t0_pred))
