from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'title':'FLASK API VERSION 1.0',
        'message':'Bienveniodo a mi API con flask'
    }
    return jsonify(context)

if __name__ == '__main__':
    app.run(debug=True)