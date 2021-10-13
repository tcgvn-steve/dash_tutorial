# -*- coding: utf-8 -*-
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])


@app.callback(
    Output('output-state', 'children'),
    Input('submit-button-state', 'n_clicks'),
    State('input-1-state', 'value'),
    State('input-2-state', 'value'),
)
def handle_with_state(n_clicks, value1, value2):
    print("=== handle_with_state === ", n_clicks, value1, value2)
    return '''
        Show value1 {} and value2 {} after clicked {} times.
    '''.format(value1, value2, n_clicks)


if __name__ == '__main__':
    app.run_server(debug=True)
