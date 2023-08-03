import dash
from dash import dcc
from dash import html
import dash_leaflet as dl
import numpy as np

app = dash.Dash(__name__)
app.title = "Sensornetz Monitoringsystem Smart City"

# Generate a sequence of a hundred data points for the line chart
x_values = np.linspace(1, 10, 100)
y_values = np.sin(x_values) + np.random.randn(100)  # Adding some randomness to the data

app.layout = html.Div([
    html.H1("Sensornetz Monitoringsystem Smart City", className='header'),

    # First Row
    html.Div(className='container', children=[
        dcc.Graph(
            id='example-graph1',
            figure={
                'data': [
                    {'values': [4, 1, 2], 'type': 'pie', 'labels': ['Data 1', 'Data 2', 'Data 3']}
                ],
                'layout': {
                    'title': 'Pie Chart'
                }
            },
            className='graph-container'
        ),

        dcc.Graph(
            id='example-graph2',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Data 2'},
                ],
                'layout': {
                    'title': 'Graph 2'
                }
            },
            className='graph-container'
        ),
    ]),

    # Second Row
    html.Div(className='container', children=[

        dl.Map(dl.TileLayer(), className='graph-container leaflet-container', center=(49.55580013470295, 7.355881155217851), zoom=19, ),

        dcc.Graph(
            id='example-graph4',
            figure={
                'data': [
                    {'x': x_values, 'y': y_values, 'type': 'line', 'name': 'Data 4'},
                ],
                'layout': {
                    'title': 'Line Graph'
                }
            },
            className='graph-container'
        ),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)

#