import tensorflow as tf
import numpy as np

def calcularRiesgo(param1,param2,param3):
    model_path = '../infrastructure/model_ml/riesgo_cardiaco_model_v1'
    loaded_model = tf.keras.models.load_model(model_path)
    new_data = np.array([[2.4,1.4,1.8,72,0,0]]) 
    # Make predictions
    prediction = loaded_model.predict(new_data)
    # Print the predictions
    return prediction
