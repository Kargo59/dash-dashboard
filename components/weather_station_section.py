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
    Temperatur
    """
    , className="text-black rounded m-5",)

def weather_data_layout():
    card_content = [
        dbc.Card(
            dbc.Row([
                dbc.Col(dbc.CardImg(src="/assets/temp.svg", top=True), width=4, className="d-flex align-items-center"),
                dbc.Col(dbc.CardBody([
                    html.H4("Temperatur", className="card-title"),
                    html.P("21°C", className="card-text")
                ]), width=8)
            ]),
            className="d-flex flex-row align-items-center m-1 p-3 border-0"
        )
        for _ in range(6)  # Creating 6 cards
    ]

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

                # Second Column with cards that display the current weather
                dbc.Col(
                    html.Div([
                        # First row of cards
                        dbc.Row([dbc.Col(card, width=6, xs=12, sm=12, md=6, lg=6, xl=6) for card in card_content[:2]]),

                        # Second row of cards
                        dbc.Row(
                            [dbc.Col(card, width=6, xs=12, sm=12, md=6, lg=6, xl=6) for card in card_content[2:4]]),

                        # Third row of cards
                        dbc.Row(
                            [dbc.Col(card, width=6, xs=12, sm=12, md=6, lg=6, xl=6) for card in card_content[4:6]]),


                    ]),
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
        # Third row
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
