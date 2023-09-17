import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_leaflet as dl

custom_icon_soil_sensor = {
    "iconUrl": "/assets/bodensensor.svg",
    "iconSize": [40, 40]  # adjust based on your SVG's size
}

custom_icon_weather_station = {
    "iconUrl": "/assets/wetterstation.svg",
    "iconSize": [40, 40]  # adjust based on your SVG's size
}


def project_description_section():
    return html.Div([
        # Project Description
        dbc.Row([
            dbc.Col(html.H1("Über das Projekt", id="projektbeschreibung", className="text-center mt-5 mb-5"), width=12)
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(dcc.Markdown("""
                Als Einstieg in das Projekt betrachten wir zunächst die Fläche an sich:
                Streuobstwiese in direkter Nähe zur Burg Lichtenberg in Thallichtenberg
                15 Äpfel- und Birnenbäume, 2 Insektennistkästen, ein Infoschild zur Streuobstwiese und eine Liegebank
                Fläche ist Teil mehrerer (Premium-)Wanderwege im Landkreis Kusel
                Eine Wetterstation
                Fünf Bodenfeuchtesensoren
                """, className="text-black bg-white rounded m-5", style={"lineHeight":"200%", "font-style":"italic"})),
                lg=6, md=12, sm=12, width=4, xl=4, xs=12
            ),
            dbc.Col(
                html.Div(html.Img(src="/assets/map_intro.png", className="img-fluid rounded mx-auto d-block w-75",
                                  alt="Responsive image")),
                lg=6, md=12, sm=12, width=4, xl=4, xs=12
            )
        ], className="", justify="center"),

        # Soil Moisture and Map
        dbc.Row(
            [                # Map
                dbc.Col(html.Div(children=[
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
                        style={'max-width': '100%'},
                        center=(49.55829631209294, 7.362626642419259),
                        zoom=17,
                        zoomControl=False,
                        dragging=False,
                        doubleClickZoom=False,
                        scrollWheelZoom=False,
                        # touchZoom=False
                    ),
                ]), className="p-5", width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),
                # Text
                dbc.Col(html.Div(children=[
                    dcc.Markdown(
                        """
                        Die ersten fünf Sensoren die im September 2023 auf der Fläche einziehen durften sollen 
                        unter anderem durch die Messung der Bodenfeuchtigkeit die Pflege und Bewässerung der 
                        Obstbäume optimieren. ...
                        """
                        ,
                        className="text-black bg-white rounded p-5", style={"lineHeight":"200%", "font-style":"italic"}),
                ], ), width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),


            ],
            className="", justify="center"),
    ]
    )
