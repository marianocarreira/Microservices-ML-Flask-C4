import tensorflow as tf
import numpy as np

def calcularRiesgo(params):
    model_path = './infrastructure/riesgo_cardiaco_model_v1'
    loaded_model = tf.keras.models.load_model(model_path)
    prediction = loaded_model.predict(params.getNumpy())
    return float(prediction[0][0])

class ModelParams():
    colesterol = ''
    presion = ''
    glucosa = ''
    edad = ''
    sobrepeso = ''
    tabaquismo = ''

    def validar(self):
        error = ""
        if not self.colesterol:
            error += " Colesterol no especificado;"
        if not self.presion:
            error += " Presion no especificada;"
        if not self.glucosa:
             error += " Glucosa no especificada;"
        if not self.edad:
             error += " Edad no especificada;"
        if not self.sobrepeso:
             error += " Sobrepeso no especificado;"
        if not self.tabaquismo:
             error += " Tabaquismo no especificado;"
        
        return error
    
    def getNumpy(self):
        return np.array([[float(self.colesterol),
                        float(self.presion),
                        float(self.glucosa),
                        float(self.edad),
                        int(self.sobrepeso),
                        int(self.tabaquismo)]])
