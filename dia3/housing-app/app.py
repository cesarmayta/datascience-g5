from flask import Flask,request,render_template
from housing_ml import HousingModel

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    housing = HousingModel()
    region_choices = list(housing.region_name.keys())
    
    precio = 0
    
    if request.method == 'POST':
        rooms = int(request.form['rooms'])
        distance = int(request.form['distance'])
        region = request.form['region_value']
        precio = housing.predict_price(region,rooms,distance)
    
    context = {
        'regiones':region_choices,
        'precio':precio
    }
    return render_template('index.html',**context)

if __name__ == '__main__':
    app.run(debug=True)