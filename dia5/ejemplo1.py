import dash
from dash import dcc,html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Hola, Dash!")
])

if __name__ == '__main__':
    app.run(debug=True)