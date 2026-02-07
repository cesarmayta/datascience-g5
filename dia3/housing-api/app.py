from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from housing_ml import HousingModel

app = Flask(__name__)

#### CONFIGURACION DE SQLALCHEMY ####
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root2025@localhost:3306/proyecto_g5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Housing(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    region = db.Column(db.String(255),nullable=False)
    rooms = db.Column(db.Integer,nullable=False)
    distance = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Double,nullable=True)
    
    def __init__(self,region,rooms,distance):
        self.rooms = rooms
        self.region = region
        self.distance = distance
        
### CREAMOS UN ESQUEMA PAARA SERIALIZAR LOS DATOS
ma = Marshmallow(app)
class HousingSchema(ma.Schema):
    id = ma.Integer()
    region = ma.String()
    rooms = ma.Integer()
    distance = ma.Integer()
    price = ma.Float()
    
## REGISTRAMOS LA TABLA EN LA BASE DE DATOS
db.create_all()
print('Base de datos creada')

@app.route('/')
def index():
    context = {
        'message':'API CON FLASK PARA HOUSING MODEL'
    }
    return jsonify(context)

@app.route('/housing',methods=['POST'])
def set_data():
    region = request.json['region']
    rooms = request.json['rooms']
    distance = request.json['distance']
    
    new_housing_model = HousingModel()
    price = new_housing_model.predict_price(region,rooms,distance)
    
    #registramos el precio en el base de datos
    new_housing = Housing(region,rooms,distance)
    new_housing.price = price
    db.session.add(new_housing)
    db.session.commit() #insert into housing...
    
    data_schema = HousingSchema()
    
    context = data_schema.dump(new_housing)
    
    return jsonify(context)

if __name__ == '__main__':
    app.run(debug=True)