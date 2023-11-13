import os
import numpy as np
import pandas as pd
from fetch_assessment.logging import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from fetch_assessment.entity import SplitingDataConfig

class Spliting_Data:
    def __init__(self,config:SplitingDataConfig):
        self.config = config

    
    def create_dataset(self,data,look_back):
        X, Y = [], []
        for i in range(len(data) - look_back):
            X.append(data[i:(i + look_back)])
            Y.append(data[i + look_back])
        return np.array(X), np.array(Y)

    def spliting_data(self,X,y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = MinMaxScaler(feature_range=(0, 1))
        X_train_scaled = np.array([scaler.fit_transform(x) for x in X_train])
        X_test_scaled = np.array([scaler.transform(x) for x in X_test])
        scaler_y = MinMaxScaler(feature_range=(0, 1))
        y_train_scaled = scaler_y.fit_transform(y_train.reshape(-1, 1))
        y_test_scaled = scaler_y.transform(y_test.reshape(-1, 1))        

        return X_train_scaled,X_test_scaled,y_train_scaled,y_test_scaled

    def saving_data(self):
        X,y=self.create_dataset(pd.read_csv(self.config.data_path).drop(["# Date"],axis=1).values,self.config.look_back)
        X_train, X_test, y_train, y_test=self.spliting_data(X,y) 
        np.save(os.path.join(self.config.root_dir,"X_train.npx"),X_train)
        np.save(os.path.join(self.config.root_dir,"X_test.npx"),X_test)
        np.save(os.path.join(self.config.root_dir,"y_train.npx"),y_train)
        np.save(os.path.join(self.config.root_dir,"y_test.npx"),y_test)