from flask import Flask,request,jsonify
import joblib
import numpy as np
import sklearn

model = joblib.load('./model/housing-ml.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

app = Flask(__name__)

def predict_price(rooms):
    rooms_sc = sc_x.transform(np.array([[rooms]]))
    prediction = model.predict(rooms_sc)
    prediction_sc = sc_y.inverse_transform(prediction) * 1000
    price = round(prediction_sc[0][0],2)
    return price

@app.route('/')
def index():
    context = {
        'title':'FLASK API VERSION 1.0',
        'message':'Bienveniodo a mi API con flask'
    }
    return jsonify(context)

@app.route('/predict',methods=['POST'])
def predict():
    rooms = request.json['rooms']
    price = predict_price(rooms)
    
    context = {
        'rooms':rooms,
        'price':price
    }
    return jsonify(context)

if __name__ == '__main__':
    app.run(debug=True)