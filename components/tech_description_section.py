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


def tech_description_section():
    return html.Div([
        # Project Description
        dbc.Row([
            dbc.Col(html.H1("Technischer Hintergrund", id="lorawan", className="text-center mt-5"), width=12)
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(html.Img(src="/assets/lorawan.png", className="img-fluid rounded mx-auto d-block w-75 mt-5",
                                  alt="Responsive image")),
                lg=6, md=12, sm=12, width=4, xl=4, xs=12
            ),
            dbc.Col(
                html.Div(dcc.Markdown("""
                                    LoRaWAN bezeichnet ein drahtloses und batteriebetriebenes System zum 
                                    verschlüsselten Datenaustausch mittels geringem Energieaufwand über weite 
                                    Strecken. Zur Datenübertragung werden einerseits Sensoren oder Messgeräte 
                                    benötigt, die Daten an ein Empfängergerät, das sogenannte Gateway, aussenden. 
                                    Die Daten werden in regelmäßigen Abständen über Radiowellen ausgesendet 
                                    und empfangen. Die Experimentierfläche an der Burg Lichtenberg gibt 
                                    den Startschuss zum Aufbau eines landkreisweiten Sensorik-Netzwerks. 
                """, className="text-black m-5", style={"lineHeight": "250%", })),
                lg=6, md=12, sm=12, width=4, xl=4, xs=12
            ),
        ], className="mb-5", justify="center"),
    ]
    )
