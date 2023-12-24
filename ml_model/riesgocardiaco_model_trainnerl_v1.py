import numpy as np
import pandas as pd
import tensorflow.keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam

#Step 1 - Get the data

#--read the file
nombre_archivo = './dataset/datos_de_pacientes_5000.csv'
data = pd.read_csv(nombre_archivo, index_col=0)
#print(data)

#Step 2 - Pre-processing data

#separo los datos de las etiquetas y de los resultados
X = data.drop(['riesgo_cardiaco'], axis='columns')
y = np.array(data['riesgo_cardiaco'])

#Separo los datos en training y testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#print(X_train)

#Escalar los datos
scaler = MinMaxScaler()

scaled_X_train = scaler.fit_transform(X_train)
scaled_X_train = pd.DataFrame(scaled_X_train, columns=X_train.columns)

scaled_X_test = scaler.fit_transform(X_test)
scaled_X_test = pd.DataFrame(scaled_X_test, columns=X_test.columns)

#print(scaled_X_train)
#print(scaled_X_test)

#Step 3 - Create neuronal network

# creo el modelo
model = Sequential()

#tiene 6 datos de entrada por el sueldo basico, antiguedad, hijos, a b c
model.add(Dense(50, input_shape=(6,), activation='relu', kernel_initializer='uniform'))
model.add(Dense(25, activation='relu', kernel_initializer='random_normal'))
model.add(Dense(35, activation='relu', kernel_initializer='random_normal'))
model.add(Dense(1, activation='relu'))

#compilo la red

model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate= 0.001),  metrics = ['accuracy'])
#model.summary()

#Step 4 - Fit the network
model.fit(scaled_X_train, y_train, verbose=2, batch_size = 10000, epochs=200)

#Step 5 - Evaluate the network
resultado = model.evaluate(scaled_X_test, y_test)

#predicciones con los datos con los que no fue entrenado
y_pred = model.predict(scaled_X_test)

for i in range(200):
  print("El riesgo verdadero es ", y_test[i])
  print("El riesgo estimado es " , y_pred[i])