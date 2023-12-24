import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#Step 1 - Get the data

#--read the file
nombre_archivo = './dataset/datos_de_pacientes_5000.csv'
data = pd.read_csv(nombre_archivo, index_col=0)
print(data)

#Step 2 

#preproceso los datos
from sklearn.model_selection import train_test_split

#utilizo codificacion onehot para la categoria
data = pd.get_dummies(data)

#separo los datos de las etiquetas de los resultados
X = data.drop(['sueldo'], axis=1)

y = np.array(data['sueldo'])

#Separo los datos en training y testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)


