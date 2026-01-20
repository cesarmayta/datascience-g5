from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hola Flask! 😎'

@app.route('/usuario/<nombre>', methods=['GET'])
def usuario(nombre):
    return f'Bienvenido, {nombre}! 👋'

@app.route('/<operacion>/<int:num1>/<int:num2>', methods=['GET'])
def operacion(operacion, num1, num2):
    if operacion == 'suma':
        resultado = num1 + num2
        return f'El resultado de la suma es {resultado}'
    elif operacion == 'resta':
        resultado = num1 - num2
        return f'El resultado de la resta es {resultado}'
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
        return f'El resultado de la multiplicación es {resultado}'
    elif operacion == 'division':
        if num2 == 0:
            return 'Error: División por cero no está permitida.'
        resultado = num1 / num2
        return f'El resultado de la división es {resultado}'
    else:
        return 'Operación no válida. Usa suma, resta, multiplicacion o division.'
    
@app.route('/html', methods=['GET'])
def html():
    return '<button>Dame click! 🚀</button>'

@app.route('/html/template', methods=['GET'])
def template():
    titulo = 'Hola Flask con Templates! 🎉'
    frameworks = ['Flask', 'Django', 'FastAPI']
    return render_template(
        'index.html',
        titulo=titulo,
        frameworks=frameworks
    )

@app.route('/json', methods=['GET'])
def json():
    return {
        'id': 1,
        'nombre': 'Miguel Angel',
        'edad': 30,
        'direccion': 'Avenida los Girasoles 123'
    }

@app.route('/json/lista', methods=['GET'])
def lista():
    return [
        {'id': 1, 'nombre': 'Miguel Angel'},
        {'id': 2, 'nombre': 'Ana María'},
        {'id': 3, 'nombre': 'Luis Fernando'}
    ]

@app.route('/hola')
def hola():
    nombre = request.args.get('nombre')
    edad = request.args.get('edad')
    return f'Hola mi nombre es {escape(nombre)} y tengo {escape(edad)} años'

if __name__ == '__main__':
    app.run(debug=True)