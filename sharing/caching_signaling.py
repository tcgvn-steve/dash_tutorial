import os
import copy
import time
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
from flask_caching import Cache

# Caching and Signaling

external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

CACHE_CONFIG = {
    # try 'filesystem' if you don't want to setup redis
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('REDIS_URL', 'redis://172.17.75.15:6379')
}
cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}


app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in all_options.keys()],
        value='America'
    ),


    # signal value to trigger callbacks
    dcc.Store(id='signal'),

    # Display values
    html.Div(id='display-1',),
    html.Div(id='display-2')


])


# perform expensive computations in this "global store"
# these computations are cached in a globally available
# redis memory store which is available across processes
# and for all time.
@cache.memoize()
def global_store():
    # simulate expensive query
    # print('Computing value with {}'.format(value))
    # returned data will be stored in redis
    return all_options


def get_data_figure(city):
    print("==== get_data_figure city ", city)
    data_stored = global_store()
    print("==== get_data_figure data_stored ", data_stored)
    # return data_stored
    return data_stored[city]


@app.callback(Output('signal', 'data'), Input('dropdown', 'value'))
def compute_value(value):
    # compute value and send a signal when done
    global_store()
    return value


@app.callback(Output('display-1', 'children'), Input('signal', 'data'))
def update_graph_1(value):
    # generate_figure gets data from `global_store`.
    # the data in `global_store` has already been computed
    # by the `compute_value` callback and the result is stored
    # in the global redis cached
    return get_data_figure(value)


@app.callback(Output('display-2', 'children'), Input('signal', 'data'))
def update_graph_2(value):
    return get_data_figure(value)


if __name__ == '__main__':
    app.run_server(debug=True)
