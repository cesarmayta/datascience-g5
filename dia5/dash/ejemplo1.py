import dash
from dash import dcc,html
from dash import Input, Output

app = dash.Dash(__name__)

@app.callback(
    Output('saludo-output', 'children'),
    Input('input-nombre', 'value')
)
def saludar(nombre):
    if nombre:
        return f'Hola, {nombre}!'
    return 'Por favor, ingresa tu nombre.'


app.layout = html.Div([
    html.H1("Hola, Dash!"),
    dcc.Input(id='input-nombre', type='text', placeholder='Escribe tu nombre'),
    html.Div(id='saludo-output')
])

if __name__ == '__main__':
    app.run(debug=True)