import dash
from dash.dependencies import Input, Output
from dash_core_components.Dropdown import Dropdown
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate
from dash_html_components.Textarea import Textarea

# edits

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
            dcc.Markdown("# Create Predictor #1"),
            dcc.Dropdown(
                id = 'dropdown-pred1',
                options = [
                    {'label': 'Normal', 'value': 'norm'},
                    {'label': 'Uniform', 'value': 'unif'},
                ],
                value = 'norm',
                style = {'width': '40%'}
            ),
            html.Div(
                id = 'norm-params',
                style = {'display': 'block'},
                hidden= True,
                children = 
                [
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
            ]),
        # ]
        ]),
    dcc.Graph(
        id='graph1-normal',
        figure = fig,
        style={'width': '50%', 'height': 300},
    ),
    dcc.Markdown("# Create Predictor #2"),
])

@app.callback(
    Output('graph1-normal', 'figure'),
    [
    Input('N-input', 'value'),
    Input('mean-input', 'value'),
    Input('sd-input', 'value')
    ]
)
def update_figure(value1, value2, value3):
    if value3 is None or value2 is None or value3 < 0 or value1 < 1 or isinstance(value1, float):
        raise PreventUpdate
    else:
        return px.histogram(generate_normal_distribution(N = value1, mean = value2, std = value3))

@app.callback(
    # [Output('N-input', 'style'),
    # Output('mean-input', 'style'),
    # Output('sd-input', 'style')
    [
    Output('norm-params', 'style')    
    ],
    Input('dropdown-pred1', 'value')
)
def dynamic_options(dropdown_value):
    if dropdown_value == 'norm':
        return [{'display': 'block'}]#, {'display': 'block'}, {'display': 'block'}]
    elif dropdown_value == 'unif':
        return [{'display': None}] #, {'display': None}, {'display': None}]

if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1')
