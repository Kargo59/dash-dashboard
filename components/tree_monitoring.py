import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.graph_objects as go
import random
import dash_leaflet as dl

custom_icon_soil_sensor = {
    "iconUrl": "/assets/bodensensor.svg",
    "iconSize": [40, 40]  # adjust based on your SVG's size
}

custom_icon_weather_station = {
    "iconUrl": "/assets/wetterstation.svg",
    "iconSize": [40, 40]  # adjust based on your SVG's size
}

def random_tree_status_color():
    return random.choice(['green', 'yellow', 'red'])


def tree_layout():
    return dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.H1("Welche Bäume müssen bewässert werden?", className="text-center mt-5 mb-5"), width=12),
                ]
            ),
            dbc.Row(  # Row for the scatter plot and SVGs
                [
                    dbc.Col(
                        html.Div(children=[
                            dl.Map([
                                dl.TileLayer(),
                                dl.Marker(
                                    position=[49.557938, 7.361618],
                                    icon=custom_icon_soil_sensor,
                                    children=[
                                        dl.Tooltip("Bodenfeuchtesensor 1"),
                                    ]
                                ),
                                dl.Marker(
                                    position=[49.558005, 7.361978],
                                    icon=custom_icon_soil_sensor,
                                    children=[
                                        dl.Tooltip("Bodenfeuchtesensor 2")
                                    ]
                                ),
                                dl.Marker(
                                    position=[49.558240, 7.362581],
                                    icon=custom_icon_soil_sensor,
                                    children=[
                                        dl.Tooltip("Bodenfeuchtesensor 3")
                                    ]
                                ),
                                dl.Marker(
                                    position=[49.558573, 7.363353],
                                    icon=custom_icon_soil_sensor,
                                    children=[
                                        dl.Tooltip("Bodenfeuchtesensor 4")
                                    ]
                                ),
                                dl.Marker(
                                    position=[49.558544, 7.363788],
                                    icon=custom_icon_soil_sensor,
                                    children=[
                                        dl.Tooltip("Bodenfeuchtesensor 5")
                                    ]
                                ),
                                dl.Marker(
                                    position=[49.558357, 7.363165],
                                    icon=custom_icon_weather_station,
                                    children=[
                                        dl.Tooltip("Wetterstation")
                                    ]
                                )
                            ],
                                className='leaflet-container',
                                style={'width': '100%'},
                                center=(49.55829631209294, 7.362626642419259),
                                zoom=17,
                                zoomControl=False,
                                dragging = False,
                                doubleClickZoom = False,
                                scrollWheelZoom = False,
                                # touchZoom=False
                            ),
                        ]), width=12  # Set width to 12 for full width
                    ),

                ],
                className='mt-5 mb-5',
                justify='center'
            ),
        ],
        className="my-section-wrapper"
    )

