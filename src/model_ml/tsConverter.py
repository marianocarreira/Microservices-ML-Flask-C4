import tensorflow as tf
from . import MODEL_RELEASE_OUTPUT_PATH_LIGH, MODEL_RELEASE_OUTPUT_PATH

# Convert the model
converter = tf.lite.TFLiteConverter.from_saved_model(MODEL_RELEASE_OUTPUT_PATH) # path to the SavedModel directory
#converter = tf.lite.TFLiteConverter.from_keras_model("../predictions_ms/infrastructure/riesgo_cardiaco_model_v1")

tflite_model = converter.convert()

# Save the model.
with open(MODEL_RELEASE_OUTPUT_PATH_LIGH, 'wb') as f:
  f.write(tflite_model)
