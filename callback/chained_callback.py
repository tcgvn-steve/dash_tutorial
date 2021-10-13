# -*- coding: utf-8 -*-
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}

app.layout = html.Div([
    html.Label("Steve Label", id='label'),
    dcc.Input(value='MTL', type='text', id='input'),
    html.Div("Result of Input", id='element'),
    html.Div("Result of Input", id='element2'),

    html.Label("City option", id='label-city'),
    dcc.RadioItems(id="city-radio",
                   options=[{'label': item, 'value': item} for item in all_options.keys()]),
    html.Label("District option", id='label-district'),
    dcc.RadioItems(id="district-radio"),
    html.Div(id='display-values')
])


@app.callback(
    Output('element', 'children'),
    Input('input', 'value')
)
def get_result(value):
    return "element covered " + value


@app.callback(
    Output('element2', 'children'),
    Input('element', 'children')
)
def get_result(value):
    return "element2 get: " + value


@app.callback(
    Output('district-radio', 'options'),
    Input('city-radio', 'value')
)
def get_result(value):
    print("==== value ", value)

    if value not in all_options.keys():
        return []
    print("==== value ", value)
    return [{'label': item, 'value': item} for item in all_options[value]]


@app.callback(
    Output('display-values', 'children'),
    Input('district-radio', 'value'),
    Input('city-radio', 'value')
)
def get_result2(district, city):
    if not district or not city:
        return 'Pls choose'
    return district + ' is in ' + city


if __name__ == '__main__':
    app.run_server(debug=True)
