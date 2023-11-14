from fetch_assessment.config.configuration import ConfigurationManager
from tensorflow.keras.models import load_model
import numpy as np
import os
import joblib

class PredictionPipleline:
    def __init__(self):
        self.config=ConfigurationManager().get_evaluating_model_config()

    def predict(self,n_days):
        current_batch=np.load(os.path.join(self.config.data_path,"X_test.npy"))[-1].copy()
        model=load_model(self.config.model_path)
        scaler = joblib.load(os.path.join(self.config.data_path,"scaler.gz"))
        future_predictions=[]

        for _ in range(n_days):
            # Predict the next time step
            current_pred = model.predict(current_batch[np.newaxis, :])[0, 0]
            
            # Append the prediction to the list
            future_predictions.append(current_pred)
            
            # Update the current batch to include the new prediction and update other features
            current_batch = np.roll(current_batch, -1, axis=0)
            # Update lagged Receipt_Count
            current_batch[-1, 0] = current_pred
            # Update other features if necessary (like date components)

            # Rescale the predictions back to the original scale
            temp_shape = np.zeros((len(future_predictions), current_batch.shape[1]))
            temp_shape[:, 0] = future_predictions
            future_predictions_rescaled = scaler.inverse_transform(temp_shape)[:, 0]
        
        return future_predictions_rescaled.tolist()

