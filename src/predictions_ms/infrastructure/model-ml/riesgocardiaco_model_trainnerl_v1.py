import numpy as np
import pandas as pd
import tensorflow.keras
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam

#---------------------------------------------------Step 1 - Obtención y visualización del dataset

#--read the file
nombre_archivo = './dataset/datos_de_pacientes_5000.csv'
data = pd.read_csv(nombre_archivo, index_col=0)
#print(data)

#Chequeo y remuevo NaNs
print("Shape antes",data.shape)
data.dropna()
print("Shape despues",data.shape)

#Analisis visual de los datos
plt.rcParams['font.size'] = 15 
f = plt.figure(figsize=(8,4))
ax = f.add_subplot(1,1,1)
data["riesgo_cardiaco"].hist(ax=ax, edgecolor='black', linewidth=2)
ax.set_xlim([-0.5, 1.5])
ax.set_xticks([0, 1])
ax.set_xticklabels(["No", "Si"])
ax.set_title("Riesgo Cardíaco S/N?")
ax.set_xlabel("Respuesta")
ax.set_ylabel("Conteo")
ax.set_ylim([0, 3000])
f.tight_layout()
plt.show()

#Dispersion Colesterol/Edad
plt.rcParams['font.size'] = 15 
f = plt.figure(figsize=(8,4))
ax = f.add_subplot(1,1,1)
ax.scatter(data["edad"], data["colesterol"], alpha=0.25)
ax.set_title("Colesterol vs. Edad")
ax.set_ylabel("Colesterol")
ax.set_xlabel("Edad")
f.tight_layout() 
plt.show()

#Dispersion Colesterol/Edad
plt.rcParams['font.size'] = 15 
f = plt.figure(figsize=(8,4))
ax = f.add_subplot(1,1,1)
ax.scatter(data["edad"], data["presion"], alpha=0.25)
ax.set_title("Colesterol vs. Presion")
ax.set_ylabel("Presion")
ax.set_xlabel("Edad")
f.tight_layout() 
plt.show()

#---------------------------------------------------Step 2 - Pre-procesar datos

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

#---------------------------------------------------Step 3 - Configurar el modelo

# creo el modelo
model = Sequential()

#tiene 6 datos de entrada por el sueldo basico, antiguedad, hijos, a b c
model.add(Dense(6, input_shape=(6,), activation='relu', kernel_initializer='uniform'))
model.add(Dense(50, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(150, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#compilo la red

model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.002),  metrics = ['accuracy'])
model.summary()

#---------------------------------------------------Step 4 - Entrenar la red

model.fit(scaled_X_train, y_train, verbose=2, batch_size = 10000, epochs=250)

#---------------------------------------------------Step 5 - Evaluar la red
resultado = model.evaluate(scaled_X_test, y_test)

#predicciones con los datos con los que no fue entrenado
y_pred = model.predict(scaled_X_test)

for i in range(10):
  print("El riesgo verdadero es ", y_test[i])
  print("El riesgo estimado es " , y_pred[i])


  model.save("../predictor-ms/business/riesgo_cardiaco_model_v1")