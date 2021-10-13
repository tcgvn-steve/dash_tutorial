import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# In the user's browser session via dcc.Store

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}

app.layout = html.Div([
    dcc.Graph(id='graph'),
    html.Table(id='table'),
    dcc.RadioItems(id="city-radio",
                   options=[{'label': item, 'value': item} for item in all_options.keys()]),
    # dcc.Store inside the app that stores the intermediate value
    html.Div(id='display-values'),
    dcc.Store(id='intermediate-value'),
])


@app.callback(
    Output('intermediate-value', 'data'),
    Input('city-radio', 'value'))
def callback_a(value):
    return 'dcc.Store {}'.format(value)


@app.callback(
    Output('display-values', 'children'),
    Input('intermediate-value', 'data'))
def callback_b(value):
    return 'Value of radio {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
