from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'message':'API CON FLASK PARA HOUSING MODEL'
    }
    return jsonify(context)

if __name__ == '__main__':
    app.run(debug=True)