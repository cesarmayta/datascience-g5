from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    resultado = None
    if request.method == 'POST':
        soles = request.form.get('soles', type=float)
        resultado = round(soles / 3.3, 2)
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)