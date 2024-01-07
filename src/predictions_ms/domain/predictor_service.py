import tensorflow as tf
import numpy as np
from infrastructure.config import config_data

def calcularRiesgo(params):
    model_path = config_data["ML_MODEL_PATH"]
    loaded_model = tf.keras.models.load_model(model_path)
    prediction = loaded_model.predict(params.getNumpy())
    return float(prediction[0][0])

def calcularRiesgoLight(params):
    # Load the TFLite model and allocate tensors.
    interpreter = tf.lite.Interpreter(model_path=config_data["ML_MODEL_PATH_LIGHT"])
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Test the model on random input data.
    input_shape = input_details[0]['shape']
    input_data = np.float32(params.getNumpy())
    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()

    # The function `get_tensor()` returns a copy of the tensor data.
    # Use `tensor()` in order to get a pointer to the tensor.
    output_data = interpreter.get_tensor(output_details[0]['index'])
    print(output_data)
    return float(output_data[0][0])


class ModelParams():
    colesterol = ''
    presion = ''
    glucosa = ''
    edad = ''
    sobrepeso = ''
    tabaquismo = ''

    def fromRequest(self, request):
        error = ''
       
        colesterol = request.args.get('colesterol')
        if not colesterol:
            error += " Colesterol no especificado;"
        else:
            self.colesterol = colesterol

        presion = request.args.get('presion')
        if not presion:
            error += " Presion no especificada;"
        else:
            self.presion=presion

        glucosa = request.args.get('glucosa')
        if not glucosa:
             error += " Glucosa no especificada;"
        else:
            self.glucosa = glucosa
        
        edad = request.args.get('edad')
        if not edad:
             error += " Edad no especificada;"
        else:
            self.edad = edad

        sobrepeso = request.args.get('sobrepeso')
        if not sobrepeso:
             error += " Sobrepeso no especificado;"
        else:
            self.sobrepeso = sobrepeso
        
        tabaquismo = request.args.get('tabaquismo')
        if not tabaquismo:
             error += " Tabaquismo no especificado;"
        else:
             self.tabaquismo = tabaquismo
        
        if  error != '':
            return { 'error': error }
        else:
            return None
    
    def getNumpy(self):
        return np.array([[float(self.colesterol),
                        float(self.presion),
                        float(self.glucosa),
                        float(self.edad),
                        int(self.sobrepeso),
                        int(self.tabaquismo)]])
