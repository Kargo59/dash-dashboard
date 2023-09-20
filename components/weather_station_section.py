from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from data_source import fetch_weatherstation_temp, fetch_weatherstation_precipitation, fetch_weatherstation_luminosity, fetch_weatherstation_humidity, fetch_weatherstation_wind_speed, fetch_weatherstation_air_pressure

#function to display the last measurement's date and time
def get_last_update_time(df):
    # Get the last time value from the dataframe
    last_time = df['time'].iloc[-1]

    # Convert it to the desired string format
    formatted_time = last_time.strftime('%d/%m/%Y %H:%M')

    # Combine with the given prefix and append "Uhr"
    return f"Letzte Aktualisierung: {formatted_time} Uhr"

# Fetch data from data_source module
df_weatherstation = fetch_weatherstation_temp() #Temperature
df_weatherstation_precipitation = fetch_weatherstation_precipitation()
df_weatherstation_luminosity = fetch_weatherstation_luminosity()
df_weatherstation_humidity = fetch_weatherstation_humidity()
df_weatherstation_wind_speed = fetch_weatherstation_wind_speed()
df_weatherstation_air_pressure = fetch_weatherstation_air_pressure()

#update the display for when the last measurement was:
last_update = get_last_update_time(df_weatherstation)
#cumulate the data for every hour so that the bars of the graph appear thicker
df_weatherstation_precipitation = df_weatherstation_precipitation.resample('H', on='time').sum().reset_index()

#cards for the live weather data
last_temperature = df_weatherstation['value'].iloc[-1]
last_precipitation = df_weatherstation_precipitation['value'].iloc[-1]
last_luminosity = df_weatherstation_luminosity['value'].iloc[-1]
last_humidity = df_weatherstation_humidity['value'].iloc[-1]
last_wind_speed = df_weatherstation_wind_speed['value'].iloc[-1]
last_air_pressure = df_weatherstation_air_pressure['value'].iloc[-1]

card_data = [
    {
        "img_src": "/assets/thermometer_color.svg",
        "title": "Temperatur",
        "value": f"{last_temperature}°C"
    },
    {
        "img_src": "/assets/humidity.svg",
        "title": "Luftfeuchte",
        "value": f"{int(last_humidity)}%"
    },
    {
        "img_src": "/assets/barometer.svg",
        "title": "Luftdruck",
        "value": f"{int(last_air_pressure / 100)} hPa"
    },
    {
        "img_src": "/assets/luminosity.svg",
        "title": "Helligkeit",
        "value": f"{int(last_luminosity)} Lux"
    },
    {
        "img_src": "/assets/wind.svg",
        "title": "Windgeschw.",
        "value": f"{int(last_wind_speed)} m/s"
    },
    {
        "img_src": "/assets/precipitation.svg",
        "title": "Niederschlag",
        "value": f"{int(last_precipitation)} mm/h"
    }
]


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
                'margin': {
                    'l': 40,  # Left margin
                    'r': 40,  # Right margin
                    'b': 80,  # Bottom margin
                    't': 40,  # Top margin
                },
                'font': {
                    'family': 'Poppins',
                },
                'title': 'Temperatur der letzten 24 Stunden',
                'autosize': True,
                # 'margin': {'t': 40, 'b': 40, 'l': 60, 'r': 50},
                'paper_bgcolor': 'rgba(0,0,0,0)',
                'width': '100%',
                'xaxis': {
                    'fixedrange': True},  # these two lines disable zoom
                'yaxis': {
                    'title': {
                        'text': 'Temperatur [°C]',
                        'standoff': 20,
                        'rotate': 0},
                    'fixedrange': True,}  # and pan
            }
        },
        config={'displayModeBar': False, 'staticPlot': False},  # staticPlot makes the entire plot static
        style={'height': '100%', 'width': '100%'}
    )

def create_precipitation_graph():
    return dcc.Graph(
        figure={
            'data': [
                {
                    'x': df_weatherstation_precipitation['time'],
                    'y': df_weatherstation_precipitation['value'],
                    'type': 'bar',
                    'name': 'Precipitation',
                    'marker': {'color': 'green'},
                }
            ],
            'layout': {
                'margin': {
                    'l': 40,  # Left margin
                    'r': 40,  # Right margin
                    'b': 80,  # Bottom margin
                    't': 40,  # Top margin
                },
                'font': {
                    'family': 'Poppins',
                },
                'title': 'Niederschlag der letzten 24 Stunden',
                'autosize': True,
                'paper_bgcolor': 'rgba(0,0,0,0)',
                'width': '100%',
                'xaxis': {'fixedrange': True},
                'yaxis': {
                    'title': {
                        'text': 'Niederschlag [mm/h]',
                        'standoff': 20,
                        'rotate': 0},
                    'fixedrange': True,
                    'range': [0, max(df_weatherstation_precipitation['value']) + 1] # +1 for a bit of space on top
                },
            }
        },
        config={'displayModeBar': False, 'staticPlot': False},
        style={'height': '100%', 'width': '100%'}
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
                dbc.Col(
                    dbc.CardImg(src=card["img_src"], top=True, style={'min-width': '35px',}, className="img-fluid p-0"),
                    width=3),
                dbc.Col([
                    html.Div(html.P(card["title"], className="font-weight-bold card-title p-0 m-0",
                                    style={'font-weight': '700'}), className="text-center"),
                    html.P(card["value"], className="card-text p-0 m-0")
                ], width=9, className='d-flex flex-column justify-content-center align-items-center pl-2')
            ]),
            className="d-flex flex-row align-items-center m-1 border-0"
        )
        for card in card_data
    ]

    return dbc.Container([
        # header
        dbc.Row([
            dbc.Col(
                html.H1("Aktuelle Wetterdaten der Wetterstation Kusel", className="text-center mt-5 mb-2", id="wetterdaten",),
                width=12),
            dbc.Col(html.P(f"({last_update})", className="text-center mb-5"), width=12)
        ]),
        # Cards Row
        dbc.Row(
            [dbc.Col(card, width=4, xs=6, sm=6, md=6,lg=4, xl=4, xxl=4) for card in card_content],
            className="mt-5 mb-5", justify="center"
        ),

        # First Graphs Row
        dbc.Row(
            [
                # First Column with temperature graph
                dbc.Col(
                    html.Div(children=[create_temperature_graph()],
                             className="mt-5"),
                    md=6, xs=12
                ),

                # Second Column with precipitation graph
                dbc.Col(
                    html.Div(children=[create_precipitation_graph()],
                             className="mt-5"),
                    md=6, xs=12
                ),
            ],
            className="", justify="center"
        ),

    ])