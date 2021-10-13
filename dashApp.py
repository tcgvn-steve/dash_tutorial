import dash
from dash import dcc 
from dash import html
import pandas as pd
import plotly.express as px


colors = {
    'background': '#757070',
    'text': '#7FDBFF'
}

dataframe = pd.DataFrame({
   "Fruit": ["Apples", "Oranges", "Apples", "Oranges", "Apples", "Oranges"],
   "Amount": [4, 1, 2, 2, 4, 5],
   "City": ["SF", "SF", "Montreal", "Montreal", "A", "A"]
})

fig = px.bar(dataframe, x="Fruit", y="Amount", color="City", barmode="group" )
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig_example ={
         'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Delhi'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Mumbai'},
         ],
         'layout': {
            'title': 'Dash Data Visualization'
         }
      }

app = dash.Dash(__name__)
app.layout = html.Div(style={'backgroundColor': colors['background']} , children=[
   html.H1('This is Steve\'s Dash',
            # The keys in the style dictionary are camelCased. So, instead of text-align, it's textAlign.
            style={
               'textAlign': 'center',
               'color': colors['text']
            }),
   html.Div('''Dash Framework: A web application framework for Python.''',
            style={
               'textAlign': 'center',
               'color': colors['text']
            }),
   dcc.Graph(
      id='example-graph',
      figure=fig
   )
])

if __name__ == '__main__':
   app.run_server(debug=True)