import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

import numpy as np
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

def generate_normal_distribution(N = 100, mean = 0, std = 1):
    return np.random.normal(loc = mean, scale = std, size = N)

normal_1 = generate_normal_distribution()

fig = px.histogram(normal_1)


app.layout = html.Div([
    html.Div([
        # children=[ 
            dcc.Input(
                id='N-input',
                type = "number",
                value = 100,
                style = {'display': 'block'}
            ), 
            dcc.Input(
                id = 'mean-input',
                type = "number",
                value = 0,
                style = {'display': 'block'}
            ),
            dcc.Input(
                id = 'sd-input',
                type = 'number',
                value = 1,
                style = {'display': 'block'}
            ),
        # ]
        ]),
    dcc.Graph(
        id='graph1-normal',
        figure = fig,
        style={'width': '50%', 'height': 300},
    )
])

@app.callback(
    Output('graph1-normal', 'figure'),
    [Input('N-input', 'value'),
     Input('mean-input', 'value'),
     Input('sd-input', 'value')]
)
def update_figure(value1, value2, value3):
    return px.histogram(generate_normal_distribution(N = value1, mean = value2, std = value3))

if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1')
