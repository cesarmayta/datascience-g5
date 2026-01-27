import joblib
import numpy as np
import sklearn

model = joblib.load('./model/housing-ml.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

rooms = int(input("Ingrese nro de habitaciones : "))
rooms_sc = sc_x.transform(np.array([[rooms]]))

prediction = model.predict(rooms_sc)
prediction_sc = sc_y.inverse_transform(prediction) * 1000
print(f'El precio para una casa de {rooms} habitaciones es de {prediction_sc[0][0]:.2f} USD')