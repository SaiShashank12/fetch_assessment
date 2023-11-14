from fetch_assessment.entity import EvaluatingModelConfig
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import LSTM,GRU, Dense,Dropout,Bidirectional,Conv1D,Reshape,MaxPooling1D,Flatten,SimpleRNN
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import joblib
import os


class ModelEvaluator:
    def __init__(self, config: EvaluatingModelConfig):
        self.config = config

    
    def evaluating(self):
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
        y_pred_train = scaler.inverse_transform(temp_shape)[:, 0]

        # Reshape y_test for inverse transformation
        y_train_temp_shape = np.zeros((len(y_train), scaled_data.shape[1]))
        y_train_temp_shape[:, 0] = y_train
        y_train_rescaled = scaler.inverse_transform(y_train_temp_shape)[:, 0]

        # Calculating RMSE on the rescaled data
        rmse = np.sqrt(mean_squared_error(y_train_rescaled, y_pred_train))
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
        y_pred_test = scaler.inverse_transform(temp_shape)[:, 0]

        # Reshape y_test for inverse transformation
        y_test_temp_shape = np.zeros((len(y_test), scaled_data.shape[1]))
        y_test_temp_shape[:, 0] = y_test
        y_test_rescaled = scaler.inverse_transform(y_test_temp_shape)[:, 0]

        # Calculating RMSE on the rescaled data
        rmse = np.sqrt(mean_squared_error(y_test_rescaled, y_pred_test))
        print("Test RMSE on original scale:", rmse)
        
        return y_train_rescaled, y_test_rescaled,y_pred_train,y_pred_test

    def plot_predictions(self, y_true, y_pred,file_name):
        plt.figure(figsize=(10, 6))
        plt.plot(y_true, label='Actual', color='blue', marker='o')
        plt.plot(y_pred, label='Predicted', color='red', marker='x')
        plt.title(file_name[:-4]+" "+'Actual vs Predicted')
        plt.xlabel('Time Steps')
        plt.ylabel('Values')
        plt.legend()
        plt.grid(True)
        plt.savefig(os.path.join(self.config.root_dir, file_name))

