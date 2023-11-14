import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import LSTM,GRU, Dense,Dropout,Bidirectional,Conv1D,Reshape,MaxPooling1D,Flatten,SimpleRNN
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib
import os
from fetch_assessment.entity import EvaluatingModelConfig

class ModelEvaluator:
    def __init__(self, config: EvaluatingModelConfig):
        self.config = config

    
    def evalating(self):
        import numpy as np

        # Load the data
        X_train = np.load(os.path.join(self.config.data_path,"X_train.npy"))
        y_train = np.load(os.path.join(self.config.data_path,"y_train.npy"))
        X_test = np.load(os.path.join(self.config.data_path,"X_test.npy"))
        y_test = np.load(os.path.join(self.config.data_path,"y_test.npy"))
        scaled_data = np.load(os.path.join(self.config.data_path,"scaled_data.npy"))
        scaler = joblib.load(os.path.join(self.config.data_path,"scaler.gz"))
        
        model=load_model(self.config.model_path)

        # Predicting on the train set
        y_pred = model.predict(X_train)
        print(y_pred.shape,y_train.shape)
        # Calculating RMSE
        rmse = np.sqrt(mean_squared_error(y_train, y_pred))
        print("Train RMSE:", rmse)

        # Reshape y_pred_scaled for inverse transformation
        temp_shape = np.zeros((len(y_pred), scaled_data.shape[1]))
        temp_shape[:, 0] = y_pred[:, 0]
        y_pred = scaler.inverse_transform(temp_shape)[:, 0]

        # Reshape y_test for inverse transformation
        y_test_temp_shape = np.zeros((len(y_train), scaled_data.shape[1]))
        y_test_temp_shape[:, 0] = y_train
        y_test_rescaled = scaler.inverse_transform(y_test_temp_shape)[:, 0]

        # Calculating RMSE on the rescaled data
        rmse = np.sqrt(mean_squared_error(y_test_rescaled, y_pred))
        print("Train RMSE on original scale:", rmse)
        
        # Predicting on the test set
        y_pred = model.predict(X_test) 
        print(y_pred.shape,y_test.shape)
        # Calculating RMSE
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        print("Test RMSE:", rmse)
        
        # Reshape y_pred_scaled for inverse transformation
        temp_shape = np.zeros((len(y_pred), scaled_data.shape[1]))
        temp_shape[:, 0] = y_pred[:, 0]
        y_pred = scaler.inverse_transform(temp_shape)[:, 0]

        # Reshape y_test for inverse transformation
        y_test_temp_shape = np.zeros((len(y_test), scaled_data.shape[1]))
        y_test_temp_shape[:, 0] = y_test
        y_test_rescaled = scaler.inverse_transform(y_test_temp_shape)[:, 0]

        # Calculating RMSE on the rescaled data
        rmse = np.sqrt(mean_squared_error(y_test_rescaled, y_pred))
        print("Test RMSE on original scale:", rmse)
        import matplotlib.pyplot as plt
        import numpy as np


        # Sample data - replace these with your actual data
        y_train_rescaled = np.random.rand(100)  # Sample training data
        y_test_rescaled = np.random.rand(50)  # Sample test data
        y_pred = np.random.rand(50)  # Sample predicted data

        # Generating indices for test data and predictions for plotting
        test_indices = np.arange(100, 150)

        # Plotting
        plt.figure(figsize=(12, 6))
        plt.plot(y_train_rescaled, label='Training Data')
        plt.plot(test_indices, y_test_rescaled, label='Test Data')
        plt.plot(test_indices, y_pred, label='Predicted Data')
        plt.xlabel('Time Steps')
        plt.ylabel('Values')
        plt.title('Comparison of Train, Test and Predicted Data')
        plt.legend()
        plt.show()



