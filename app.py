import dash
from dash import dcc
from dash import html
import dash_leaflet as dl
import numpy as np
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO, "/assets/style.css"], assets_folder='assets')
app.title = "Sensornetz Monitoringsystem Smart City"

# Generate a sequence of a hundred data points for the line chart
x_values = np.linspace(1, 10, 100)
y_values = np.sin(x_values) + np.random.randn(100)  # Adding some randomness to the data

app.layout = html.Div([
    html.H1("Sensornetz Monitoringsystem Smart City", className='header'),

    # First Row
    html.Div(className='container', style={'max-width': '90%'}, children=[
        dcc.Graph(
            id='graph1',
            figure={
                'data': [
                    {'values': [4, 1, 2], 'type': 'pie', 'labels': ['Data 1', 'Data 2', 'Data 3']}
                ],
                'layout': {
                    'title': 'Pie Chart',
                    'paper_bgcolor': 'rgba(0,0,0,0)',
                }
            },
            className='graph-container',
        ),
        html.Div(
            id='temperature-humidity',
            children=[
                html.P("Aktuelle Wetterdaten:", style={'text-align': 'center'}),
                html.P("Temperatur: 10°C"),
                html.P("Niederschlag: 3 mm"),
                html.P("Luftfeuchtigkeit: 22 %"),
                html.P("Windgeschwindigkeit: 2 m/s"),
                html.P("Windrichtung: NW"),
                html.P("letzte Aktualisierung: 28/08/2023 08:00:00", style={'text-align': 'right', 'font-size': '13px', 'margin-right': '20px'}),
            ],
            className='graph-container info-container'
        ),
        dcc.Graph(
            figure={
                'data': [
                    {'x': x_values, 'y': y_values, 'type': 'line', 'name': 'Data 4'},
                ],
                'layout': {
                    'title': 'Temperatur der letzten 30 Tage',
                    'paper_bgcolor': 'rgba(0,0,0,0)',
                }
            },
            className='graph-container'
        ),

        dcc.Graph(
            figure={
                'data': [
                    {'x': [1, 2, 3, 4, 5, 6, 7], 'y': [2, 4, 5, 2, 7, 8, 2], 'type': 'bar', 'name': 'Data 2'},
                ],
                'layout': {
                    'title': 'Niederschlag der letzten 30 Tage',
                    'paper_bgcolor': 'rgba(0,0,0,0)'
                }
            },
            className='graph-container'
        ),

        # Leaflet Map (moved from second row)
        dl.Map([
            dl.TileLayer(),
            dl.Marker(
                position=[49.557938, 7.361618],
                children=[
                    dl.Tooltip("Bodenfeuchtesensor 1")
                ]
            ),
            dl.Marker(
                position=[49.558005, 7.361978],
                children=[
                    dl.Tooltip("Bodenfeuchtesensor 2")
                ]
            ),
            dl.Marker(
                position=[49.558240, 7.362581],
                children=[
                    dl.Tooltip("Bodenfeuchtesensor 3")
                ]
            ),
            dl.Marker(
                position=[49.558573, 7.363353],
                children=[
                    dl.Tooltip("Bodenfeuchtesensor 4")
                ]
            ),
            dl.Marker(
                position=[49.558544, 7.363788],
                children=[
                    dl.Tooltip("Bodenfeuchtesensor 5")
                ]
            ),
            dl.Marker(
                position=[49.558357, 7.363165],
                children=[
                    dl.Tooltip("Wetterstation")
                ]
            )
        ],
            className='graph-container leaflet-container',
            style={'max-width': '100%'},
            center=(49.556846, 7.358865),
            zoom=16
        ),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
