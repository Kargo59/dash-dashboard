from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from data_source import fetch_weatherstation_temp, fetch_weatherstation_precipitation

# Fetch data from data_source module
df_weatherstation = fetch_weatherstation_temp()
df_weatherstation_precipitation = fetch_weatherstation_precipitation()

def create_temperature_graph():
    return dcc.Graph(
        figure={
            'data': [
                {
                    'x': df_weatherstation['time'],
                    'y': df_weatherstation['value'],
                    'type': 'line',
                    'name': 'Temperature'
                }
            ],
            'layout': {
                'title': 'Temperatur der letzten 24 Stunden',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                'width': '100%',
            }
        }
    )

def create_precipitation_graph():
    return dcc.Graph(
        figure={
            'data': [
                {
                    'x': df_weatherstation_precipitation['time'],
                    'y': df_weatherstation_precipitation['value'],
                    'type': 'line',
                    'name': 'Precipitation',
                    'line': {'color': 'red'}
                }
            ],
            'layout': {
                'title': 'Niederschlag der letzten 24 Stunden',
                'paper_bgcolor': 'rgba(0,0,0,0)',
                'width': '100%',
            }
        }
    )

weather_text_content = dcc.Markdown(
    """
Die Wetterstation wurde im September 2023 installiert und durch die verschiedenen Graphen können ihre Messwerte abgelesen werden. Diese beschreiben wir im Folgenden. Die Wetterstation misst:
-	die Lufttemperatur in Grad Celsius und gibt damit an, wie warm oder kalt ihre Umgebung ist.
-	die Luftfeuchte in Prozent. Im Durchschnitt liegt die Luftfeuchtigkeit in Deutschland bei 70 Prozent im Sommer und 85 Prozent im Winter.
-	den Luftdruck in Pascal. Ein hoher Luftdruck lässt in der Regel auf schönes Wetter schließen, während ein Abfall des Luftdrucks auf ein nahendes Wettertief hindeutet.
-	die Helligkeit der Fläche in Lux. 
-	die Windrichtung in Grad und -geschwindigkeit in Metern pro Sekunde. Diese geben an aus welcher Richtung (Norden, Süde, Osten, Westen) der Wind kommt und wie schnell sich die Luft auf der Fläche bewegt.
-	die Niederschlagsmenge in Millimetern pro Stunde gibt Aufschluss, ob und wie viel es auf der Fläche innerhalb einer Stunde geregnet hat.
-	den UV-Index ist ein Maß für ultraviolette Strahlung. Diese Stärke der UV-Strahlung wird primär vom Sonnenstand bestimmt. Je höher der UV-Index desto höher ist auch das Risiko für Sonnenbrand. Ab Werten von 3 und höher wird Sonnenschutz empfohlen. 
Anhand der einzelnen Wetterdaten sollen Wetterphänomene und -lagen im Landkreis Kusel sowie Zusammenhänge zwischen den Messdaten verständlich erklärbar und sichtbar gemacht werden.

    """
    , className="text-black rounded m-5",)

weather_now_text_content = dcc.Markdown(
    """
Aktuelle Bedingungen: 
-	die Lufttemperatur:
-	die Luftfeuchte:
-	den Luftdruck:
-	die Helligkeit der Fläche:
-	die Windrichtung in Grad und -geschwindigkeit:
-	die Niederschlagsmenge:
-	den UV-Index:

    """
    , className="text-black rounded m-5",)

def weather_data_layout():
    return html.Div([
        # header
        dbc.Row(dbc.Col(html.H1("Wetterdaten", className="text-center p-5", id="wetterdaten"), width=12)),

        # First row
        dbc.Row(
            [
                # First Column with weather text
                dbc.Col(
                    html.Div(children=[weather_text_content],
                             className="text-black bg-white rounded m-5"),
                    width=4, xs=12, sm=12, md=12, lg=6, xl=4,
                ),

                # Second Column with duplicate weather text
                dbc.Col(
                    html.Div(children=dbc.Card(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.CardImg(
                                            src="/assets/wetterstation.svg",
                                            className="img-fluid rounded-start",
                                        ),
                                        className="col-md-4",
                                    ),
                                    dbc.Col(
                                        dbc.CardBody(
                                            [
                                                html.H4("Temperatur", className="card-title"),
                                                weather_now_text_content
                                            ]
                                        ),
                                        className="col-md-8",
                                    ),
                                ],
                                className="g-0 d-flex align-items-center",
                            )
                        ],
                        className="mb-3",
                        style={"maxWidth": "540px"},
                    ),
                        className="text-black rounded m-5 d-flex align-items-center justify-content-center",
                    ),
                    width=4, xs=12, sm=12, md=12, lg=6, xl=4,
                ),
            ],
            className="", justify="center"
        ),

        # Second row
        dbc.Row(
            [
                # First Column with temperature graph
                dbc.Col(
                    html.Div(children=[create_temperature_graph()],
                             className="m-5"),
                    width=4, xs=12, sm=12, md=12, lg=6, xl=4,
                ),

                # Second Column with precipitation graph
                dbc.Col(
                    html.Div(children=[create_precipitation_graph()],
                             className="m-5"),
                    width=4, xs=12, sm=12, md=12, lg=6, xl=4,
                ),
            ],
            className="", justify="center"
        ),
    ])
