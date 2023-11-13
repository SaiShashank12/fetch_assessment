import os
import numpy as np
import pandas as pd
from fetch_assessment.logging import logger
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from fetch_assessment.entity import SplitingDataConfig
import joblib

class Spliting_Data:
    def __init__(self,config:SplitingDataConfig):
        self.config = config

    
    def create_dataset(self,data,look_back):
        X, Y = [], []
        for i in range(len(data) - look_back):
            X.append(data[i:(i + look_back)])
            Y.append(data[i + look_back, 0])
        return np.array(X), np.array(Y)

    def spliting_data(self,X,y):
        return train_test_split(X, y, test_size=0.2, random_state=42)
    
    def saving_data(self):
        df=pd.read_csv(self.config.data_path)
        print(len(df))
        scaler=MinMaxScaler(feature_range=(0,1))
        scaler_data=scaler.fit_transform(df.drop(["# Date"],axis=1))
        X,y=self.create_dataset(scaler_data,self.config.look_back)
        X_train, X_test, y_train, y_test=self.spliting_data(X,y) 
        print(X_train.shape, y_train.shape,X_test.shape,y_test.shape)
        np.save(os.path.join(self.config.root_dir,"scaled_data"),scaler_data)
        joblib.dump(scaler, os.path.join(self.config.root_dir,'scaler.gz'))
        np.save(os.path.join(self.config.root_dir,"X_train"),X_train)
        np.save(os.path.join(self.config.root_dir,"X_test"),X_test)
        np.save(os.path.join(self.config.root_dir,"y_train"),y_train)
        np.save(os.path.join(self.config.root_dir,"y_test"),y_test)
        