import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    print("==== selected_year ", selected_year)
    print("==== df.year ", df.year)

    filtered_df = df[df.year == selected_year]
    print("==== filtered_df ", filtered_df)

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=300)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
