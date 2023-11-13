import pandas as pd
import os
from fetch_assessment.entity import FeatureengineeringConfig

class Featureengineering:
    def __init__(self,config:FeatureengineeringConfig):
        self.config = config
    
    def add_feature(self,data):
        # Feature Engineering
        data['# Date'] = pd.to_datetime(data['# Date'])
        data['Day_of_Week'] = data['# Date'].dt.dayofweek  # Monday=0, Sunday=6
        data['Month'] = data['# Date'].dt.month
        data['Day'] = data['# Date'].dt.day
        data['Year'] = data['# Date'].dt.year

        # For simplicity, we'll create lagged features for the previous 1, 2, and 3 days.
        # These are basic lag features; more sophisticated approaches can be used for time series forecasting.
        data['Lag_1'] = data['Receipt_Count'].shift(1)
        data['Lag_2'] = data['Receipt_Count'].shift(2)
        data['Lag_3'] = data['Receipt_Count'].shift(3)
        
        return data 

    def features(self):
        data=pd.read_csv(self.config.data_path)
        data_transformed=self.add_feature(data)
        data_transformed.to_csv(os.path.join(self.config.root_dir,"data.csv"))       
