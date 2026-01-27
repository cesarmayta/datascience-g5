from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import joblib
import numpy as np
import sklearn

model = joblib.load('./model/housing-ml.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

app = Flask(__name__)

#### CONFIGURACION DE SQLALCHEMY ####
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root2025@localhost:3306/db_g5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Housing(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    rooms = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Double,nullable=True)
    
    def __init__(self,rooms):
        self.rooms = rooms
        
### CREAMOS UN ESQUEMA PAARA SERIALIZAR LOS DATOS
ma = Marshmallow(app)
class HousingSchema(ma.Schema):
    id = ma.Integer()
    rooms = ma.Integer()
    price = ma.Float()
    
## REGISTRAMOS LA TABLA EN LA BASE DE DATOS
db.create_all()
print('Base de datos creada')

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

@app.route('/housing',methods=['POST'])
def predict():
    rooms = request.json['rooms']
    price = predict_price(rooms)
    
    #registramos el precio en el base de datos
    new_housing = Housing(rooms)
    new_housing.price = price
    db.session.add(new_housing)
    db.session.commit()
    
    data_schema = HousingSchema()
    
    context = data_schema.dump(new_housing)
    
    return jsonify(context)

@app.route('/housing',methods=['GET'])
def get_data():
    data = Housing.query.all()
    data_schema = HousingSchema(many=True)
    return jsonify(data_schema.dump(data))

if __name__ == '__main__':
    app.run(debug=True)