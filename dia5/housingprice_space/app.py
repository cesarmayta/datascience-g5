import joblib
import numpy as np
import gradio as gr

modelo_housing = joblib.load('housing-ml.pkl')
scaler_x = joblib.load('scaler_x.pkl')
scaler_y = joblib.load('scaler_y.pkl')

def predict_price(rooms):
  data = np.array([[rooms]])
  data_scaled = scaler_x.transform(data)
  prediction_scaled = modelo_housing.predict(data_scaled)
  prediction = scaler_y.inverse_transform(prediction_scaled.reshape(-1,1))
  return round(prediction[0][0])*10000

demo = gr.Interface(
    fn=predict_price,
    inputs=gr.Textbox(label='nro habitaciones'),
    outputs=gr.Textbox(label='precio promedio')
)

demo.launch()