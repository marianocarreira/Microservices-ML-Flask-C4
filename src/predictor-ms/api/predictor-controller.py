import tensorflow as tf
import numpy as np

model_path = './ml_model/riesgo_cardiaco_model_v1'
loaded_model = tf.keras.models.load_model(model_path)

new_data = np.array([[2.4,1.4,1.8,72,0,0],[2.2,1.1,0.6,73,0,1]]) 

# Make predictions
predictions = loaded_model.predict(new_data)

# Print the predictions
print(predictions)