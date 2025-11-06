import dash
from dash import dcc,html
import pandas as pandas
import plotly.express as px
import seaborn as sns

df = sns.load_dataset("penguins")

app = dash.Dash(__name__)




app.layout = html.Div([
    html.H1("mi primer gráfico con Dash"),
    dcc.Graph(
        figure=px.scatter(df,x='bill_length_mm',y='bill_depth_mm',color='species',
                          title='Relación entre largo y profundidad del pico de los pingüinos')
    )
])

if __name__ == '__main__':
    app.run(debug=True)