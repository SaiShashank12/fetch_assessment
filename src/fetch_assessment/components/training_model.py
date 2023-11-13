import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,GRU, Dense,Dropout,Bidirectional,Conv1D,Reshape,MaxPooling1D,Flatten,SimpleRNN
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from fetch_assessment.entity import TrainingModelConfig
import numpy as np
import joblib
import os



class ModelTrainer:
    def __init__(self, config: TrainingModelConfig):
        self.config = config

    
    def rmse_funct(self,y_true, y_pred):
        return tf.sqrt(tf.reduce_mean(tf.square(y_true - y_pred)))

    
    def training(self):
        import numpy as np

        # Load the data
        X_train = np.load(os.path.join(self.config.data_path,"X_train.npy"))
        y_train = np.load(os.path.join(self.config.data_path,"y_train.npy"))
        
        # X_loaded and Y_loaded are now numpy arrays with the same content and shape as the original X and Y
        early_stopping = EarlyStopping(monitor='val_loss', min_delta=0.001, patience=10, restore_best_weights=True)

        model = Sequential()
        # CNN Layer
        model.add(Conv1D(filters=64, kernel_size=2, activation='relu', input_shape=(self.config.look_back, X_train.shape[2])))
        # Removing MaxPooling1D layer to maintain the sequence length
        # LSTM Layer
        model.add(LSTM(50, activation='relu', return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(50, activation='relu'))
        model.add(Dropout(0.2))
        # Output Layer
        model.add(Dense(1))

        # Compile the model
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Early stopping callback
        early_stopping = EarlyStopping(monitor='val_loss', min_delta=0.001, patience=10, restore_best_weights=True)

        # Train the model
        history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, callbacks=[early_stopping])
        model.save(self.config.model_path)
        