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

custom_icon_meadow = {
    "iconUrl": "/assets/meadow.svg",
    "iconSize": [40, 40]  # adjust based on your SVG's size
}

custom_icon_castle = {
    "iconUrl": "/assets/castle.svg",
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
                    **Zur Experimentierfläche**
                    
                    Die Streuobstwiese befindet sich in direkter Nähe zur Burg Lichtenberg in Thallichtenberg 
                    und umfasst 15 Äpfel- und Birnenbäume sowie 2 Insektennistkästen und eine Liegebank. 
                    Die Experimentierfläche liegt direkt an mehreren (Premium-)Wanderwegen. 
                    Im Rahmen von LAND L(i)EBEN werden die Experimentierfläche und das umliegende Gelände nun
                    mithilfe von Messtechnik ausgestattet, um verschiedenste Umweltwerte zu überwachen. 

                    
                    **Die Ziele**
                    
                    Mithilfe der Messungen der Bodenfeuchte kann sichergestellt werden, dass die Obstbäume 
                    auch im Sommer mit ausreichend Wasser versorgt sind und zu großen, fruchttragenden 
                    Schattenspendern heranwachsen. Doch nicht nur für uns Menschen kann die Experimentierfläche 
                    ein gemütlicher Ruheort werden, auch für die heimischen Tiere und Pflanzen bietet sie einen 
                    vielfältigen Lebensraum. Gleichzeitig bietet die Experimentierfläche ihren Gästen neue 
                    und bisher unbekannte Einblicke in unsere Natur und lädt dazu ein diese zu erforschen.

                """, className="text-black m-5", style={"lineHeight":"250%", })),
                lg=6, md=12, sm=12, width=4, xl=4, xs=12
            ),
            dbc.Col([
                html.Div(html.Img(src="/assets/map_intro.png", className="img-fluid rounded mx-auto d-block w-75 mt-5",
                                  alt="Responsive image")),
                html.Div(children=[
                    html.Div([
                        html.Img(src=custom_icon_castle["iconUrl"],
                                 style={"width": "50px", "height": "50px", "marginRight": "5px",
                                        "verticalAlign": "middle"}),
                        html.Span("Burg Lichtenberg", style={"verticalAlign": "middle"}),
                    ], className="mb-3 text-end"),
                    html.Div([
                        html.Img(src=custom_icon_meadow["iconUrl"],
                                 style={"width": "40px", "height": "40px", "marginRight": "19px",
                                        "verticalAlign": "middle"}),
                        html.Span("Streuobstwiese", style={"verticalAlign": "middle"}),
                    ]),
                ], className="text-black bg-white rounded p-5 text-end", style={"lineHeight": "250%"})
            ], lg=6, md=12, sm=12, width=4, xl=4, xs=12),

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
                        center=(49.556826530841, 7.358929023309045),
                        zoom=16,
                        zoomControl=True,
                        dragging=True,
                        doubleClickZoom=False,
                        scrollWheelZoom=False,
                        # touchZoom=False
                    ),
                ]), className="p-5", width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),

                #Accordeon Section
                dbc.Col(
                        html.Div([
                            html.P("Aktuell befinden sich folgende Messgeräte auf der Fläche:", className="mb-3"),
                            dbc.Accordion(
                                [
                                dbc.AccordionItem(
                                    [
                                        # Description
                                        dbc.Row([
                                            dbc.Col(
                                                html.Div([
                                                    html.P("Diese misst:", className="mb-3"),
                                                    html.Ul([
                                                        html.Li("die Lufttemperatur in Grad Celsius und gibt damit an, wie warm oder kalt ihre Umgebung ist."),
                                                        html.Br(),
                                                        html.Li("die Luftfeuchte in Prozent. Im Durchschnitt liegt die Luftfeuchtigkeit in Deutschland bei 70 Prozent im Sommer und 85 Prozent im Winter."),
                                                        html.Br(),
                                                        html.Li("den Luftdruck in Pascal. Ein hoher Luftdruck lässt in der Regel auf schönes Wetter schließen, während ein Abfall des Luftdrucks auf ein nahendes Wettertief hindeutet."),
                                                        html.Br(),
                                                        html.Li("die Helligkeit der Fläche in Lux."),
                                                        html.Br(),
                                                        html.Li("die Windrichtung in Grad und -geschwindigkeit in Metern pro Sekunde. Diese geben an aus welcher Richtung (Norden, Süde, Osten, Westen) der Wind kommt und wie schnell sich die Luft auf der Fläche bewegt."),
                                                        html.Br(),
                                                        html.Li("die Niederschlagsmenge in Millimetern pro Stunde gibt Aufschluss, ob und wie viel es auf der Fläche innerhalb einer Stunde geregnet hat."),
                                                        html.Br(),
                                                        html.Li("den UV-Index ist ein Maß für ultraviolette Strahlung. Diese Stärke der UV-Strahlung wird primär vom Sonnenstand bestimmt. Je höher der UV-Index desto höher ist auch das Risiko für Sonnenbrand. Ab Werten von 3 und höher wird Sonnenschutz empfohlen."),
                                                    ])]),
                                                lg=12, md=12, sm=12, width=12, xl=12, xs=12
                                            ),

                                        ], className="", justify="center"),
                                    ],
                                    title="Eine Wetterstation",
                                ),
                                # Add other accordion items as necessary
                                dbc.AccordionItem(
                                    [
                                        # Description
                                        dbc.Row([
                                            dbc.Col(
                                                html.Div([
                                                    html.P("Diese messen:", className="mb-3"),
                                                    html.Ul([
                                                        html.Li("die Bodenfeuchte in Prozent. Diese ist für die Versorgung der Obstbäume mit ausreichend Wasser von hoher Bedeutung. Ist der Boden zu trocken, können keine Photosynthese und kein Baumwachstum stattfinden. Mithilfe der Sensoren soll nicht nur ein zu trockener Boden, sondern auch eine übermäßige Bewässerung verhindert und damit Wasser eingespart werden. Die Sensoren sind in 30 Zentimetern Tiefe angebracht. "),
                                                        html.Br(),
                                                        html.Li("die Bodentemperatur in Grad Celsius. Unter 5 Grad Celsius sollte von einer Pflanzung abgesehen werden, unter 0 Grad Celsius spricht man von Bodenfrost."),
                                                        html.Br(),
                                                        html.Li("Die elektrische Leitfähigkeit in Mikrosiemens pro Zentimeter gibt Aufschluss über den Nährstoffgehalt des Bodens und zeigt den Düngebedarf sowie die Bewässerung des Bodens an. Bei einem Wert unter 0,3 Mikrosiemens pro Zentimeter sollte der Boden gedüngt werden. Ein Wert von 0,8 Mikrosiemens pro Zentimeter deutet auf eine Überdüngung hin, was die Fähigkeit der Pflanzen Nährstoffe und Wasser aufzunehmen und damit auch das Wachstum hemmt."),
                                                    ])]),
                                                lg=12, md=12, sm=12, width=12, xl=12, xs=12
                                            ),
                                        ], className="", justify="center"),
                                    ],
                                    title="Fünf Bodenfeuchtesensoren",
                                ),
                            ],
                            start_collapsed=True)],
                        className="p-5"
                    ),
                    width=4, xs=12, sm=12, md=12, lg=6, xl=4,
                ),

                # # Text
                # dbc.Col(html.Div(children=[
                #     html.Div([
                #         html.Div([
                #             html.P("Aktuell befinden sich folgende Messgeräte auf der Fläche:", className="mb-3"),
                #             html.Img(src=custom_icon_weather_station["iconUrl"],
                #                      style={"width": "40px", "height": "40px", "marginRight": "5px",
                #                             "verticalAlign": "middle"}),
                #             "Eine Wetterstation"
                #         ]),
                #         html.Div([
                #             html.Img(src=custom_icon_soil_sensor["iconUrl"],
                #                      style={"width": "40px", "height": "40px", "marginRight": "5px",
                #                             "verticalAlign": "middle"}),
                #             "Fünf Bodenfeuchtesensoren",
                #         ]),
                #     ], className="text-black bg-white rounded p-5", style={"lineHeight": "250%"}),
                #
                # ], ), width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),


            ],
            className="", justify="center"),
    ]
    )
