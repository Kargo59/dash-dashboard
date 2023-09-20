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
                    **Die Fläche**
                    
                    Die Streuobstwiese befindet sich in direkter Nähe zur Burg Lichtenberg in Thallichtenberg und umfasst 15 Äpfel- und 
                    Birnenbäume sowie 2 Insektennistkästen und eine Liegebank. Die Fläche liegt direkt an mehreren (Premium-)Wanderwegen.
                    Im Rahmen von LAND L(i)EBEN wird die Fläche nun nach und nach mithilfe von Sensorik ausgestattet und so 
                    verschiedenste Umweltwerte auf der Fläche überwacht. 
                    
                    **Zweck**
                    
                    Mithilfe der Messungen möchten wir versteckte Vorgänge, 
                    wie die Speicherung von Wasser im Boden sichtbar machen. So soll verhindert werden, dass die 
                    Obstbäume im Sommer verdursten und die Fläche langfristig als schattiger Picknick-Platz heranwachsen. Doch nicht nur 
                    für die Menschen kann die Fläche ein gemütlicher Ruheort werden, auch für die heimischen Tiere und Pflanzen bietet sie 
                    einen vielfältigen Lebensraum. Gleichzeitig bietet die Fläche ihren Gästen die Chance, bisher Unbekanntes an ihrer 
                    Umwelt zu erforschen und allerlei Neues zu entdecken.

                """, className="text-black m-5", style={"lineHeight":"250%", })),
                lg=6, md=12, sm=12, width=4, xl=4, xs=12
            ),
            dbc.Col(
                html.Div(html.Img(src="/assets/map_intro.png", className="img-fluid rounded mx-auto d-block w-75 mt-5",
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
                            position=[49.55733911301222, 7.3607157322857075],
                            icon=custom_icon_soil_sensor,
                            children=[
                                dl.Tooltip("Bodenfeuchtesensor 1"),
                            ]
                        ),
                        dl.Marker(
                            position=[49.55751276556591, 7.361085800771698],
                            icon=custom_icon_soil_sensor,
                            children=[
                                dl.Tooltip("Bodenfeuchtesensor 2")
                            ]
                        ),
                        dl.Marker(
                            position=[49.55765249375624, 7.361099770403598],
                            icon=custom_icon_soil_sensor,
                            children=[
                                dl.Tooltip("Bodenfeuchtesensor 3")
                            ]
                        ),
                        dl.Marker(
                            position=[49.55763383926781, 7.36134283963924],
                            icon=custom_icon_soil_sensor,
                            children=[
                                dl.Tooltip("Bodenfeuchtesensor 4")
                            ]
                        ),
                        dl.Marker(
                            position=[49.55780646950395, 7.361366709398196],
                            icon=custom_icon_soil_sensor,
                            children=[
                                dl.Tooltip("Bodenfeuchtesensor 5")
                            ]
                        ),
                        dl.Marker(
                            position=[49.5576136818875, 7.36157382546307],
                            icon=custom_icon_weather_station,
                            children=[
                                dl.Tooltip("Wetterstation")
                            ]
                        )

                    ],
                        className='leaflet-container',
                        style={'max-width': '100%'},
                        center=(49.557488461793795, 7.36099355082976),
                        zoom=18,
                        zoomControl=True,
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
                        Aktuell befinden sich folgende Messgeräte auf der Fläche:
                        -	Eine Wetterstation
                        -	Fünf Bodenfeuchtesensoren

                        """
                        ,
                        className="text-black bg-white rounded p-5", style={"lineHeight":"250%",}),
                ], ), width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),


            ],
            className="", justify="center"),
    ]
    )
