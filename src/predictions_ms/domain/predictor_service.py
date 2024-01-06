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
