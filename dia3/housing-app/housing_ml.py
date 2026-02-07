import joblib
import numpy as np
import sklearn

# Load the best model and scalers
model = joblib.load('./model/model.pkl')
scaler_X = joblib.load('./model/scaler_X.pkl')
scaler_y = joblib.load('./model/scaler_y.pkl')


class HousingModel:
  
  def __init__(self):
    self.region_name = {
      'Northern Metropolitan': [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
      'Western Metropolitan': [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],
      'Southern Metropolitan': [0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0],
      'South-Eastern Metropolitan': [0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],
      'Eastern Metropolitan': [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0],
      'Northern Victoria': [0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],
      'Eastern Victoria': [0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],
      'Western Victoria': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0]
    }
    

  def predict_price(self,region,rooms,distance):
    # Ensure new_data is a 2D array for scaling
    data_list = self.region_name[region] + [rooms,distance]
    new_house_data = np.array(data_list)
    new_data_array = np.array(new_house_data).reshape(1, -1)

    # Scale the input data
    new_data_scaled = scaler_X.transform(new_data_array)
    # Make prediction using the model
    prediction_scaled = model.predict(new_data_scaled)
    # Inverse transform the prediction to get original price scale
    prediction = scaler_y.inverse_transform(prediction_scaled.reshape(1, -1))

    return round(prediction[0][0],2) * 1000000


# region = 'Western Metropolitan'
# rooms = 3
# distance = 5

# new_housing = HousingModel()

# predicted_price = new_housing.predict_price(region,rooms,distance)
# print(f"Predicted Price: {predicted_price:.3f} EUROS")