from dash.dependencies import Output
import dash_core_components as dcc
import dash
from dash import html
import pandas as pd
from dash.dependencies import Input, Output


app = dash.Dash(__name__)


def render_naviagte():
    return html.Div([
        html.Br(),
        dcc.Link("Navigate to / ", href='/'),
        html.Br(),
        dcc.Link("Navigate to /steve ", href='/steve'),
        html.Br(),
        dcc.Link("Navigate to /company ", href='/company'),
    ])


app.layout = html.Div([
    dcc.Location(id='url'),
    render_naviagte(),
    html.Div(id='content'),

])


def render_personal_page():
    return html.Div([
        html.H4(children='Here you are personal Page'),
        html.H4(children='US Agriculture Exports (2011)'),
        html.Div(children="Steve", className='app-header'),
        html.Div(children="Steve", className=''),
        html.Div([
            html.H1("Tutotials about ui"),
            html.P("This is p element"),
            html.P("This is p element")
        ]),
    ])


def render_company_page():
    return html.Div([
        html.H4(children='Here you are company Page'),
        html.H4(children='US Agriculture Exports (2011)'),
        html.Div(children="Steve", className='app-header'),
        html.Div(children="Steve", className=''),
        html.Div([
            html.H1("Tutotials about ui"),
            html.P("This is p element"),
            html.P("This is p element")
        ]),
    ])


# validate for page don't show when initiation
app.validation_layout = html.Div([
    render_naviagte(),
    render_company_page(),
    render_personal_page(),
])


@app.callback(
    Output('content', 'children'),
    Input('url', 'pathname')
)
def display(pathname):
    if pathname == '/':
        return html.Div([
            html.Br(),
            html.H4(children='Here you are Home Page'),
        ])
    if pathname == '/steve':
        return render_personal_page()

    if pathname == '/company':
        return render_company_page()


if __name__ == '__main__':
    app.run_server(debug=True)
