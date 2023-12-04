import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_leaflet as dl
from data_source import fetch_soil_water_1, fetch_soil_water_2, fetch_soil_water_3, fetch_soil_water_4, fetch_soil_water_5
from components.weather_station_section import df_weatherstation_precipitation
from datetime import datetime, timedelta
import random



df_soil_moisture_1 = fetch_soil_water_1()
df_soil_moisture_2 = fetch_soil_water_2()
df_soil_moisture_3 = fetch_soil_water_3()
df_soil_moisture_4 = fetch_soil_water_4()
df_soil_moisture_5 = fetch_soil_water_5()



custom_icon_soil_sensor = {
    "iconUrl": "/assets/bodensensor.svg",
    "iconSize": [40, 40]
}

custom_icon_weather_station = {
    "iconUrl": "/assets/wetterstation.svg",
    "iconSize": [40, 40]
}

green_tree = {
    "iconUrl": "/assets/green_tree.svg",
    "iconSize": [40, 40]
}

yellow_tree = {
    "iconUrl": "/assets/yellow_tree.svg",
    "iconSize": [40, 40]
}

red_tree = {
    "iconUrl": "/assets/red_tree.svg",
    "iconSize": [40, 40]
}

def get_tree_icon(value):
    if value > 20:
        return green_tree
    elif 10 <= value <= 20:
        return yellow_tree
    else:
        return red_tree

#get the last value from the database, if there are no values at all, set the default value at 31
try:
    last_value_soil_sensor_1 = df_soil_moisture_1['value'].iloc[-1]
except IndexError:
    last_value_soil_sensor_1 = 31

tree_icon_1 = get_tree_icon(float(last_value_soil_sensor_1))

try:
    last_value_soil_sensor_2 = df_soil_moisture_2['value'].iloc[-1]
except IndexError:
    last_value_soil_sensor_2 = 31

tree_icon_2 = get_tree_icon(float(last_value_soil_sensor_2))

try:
    last_value_soil_sensor_3 = df_soil_moisture_3['value'].iloc[-1]
except IndexError:
    last_value_soil_sensor_3 = 31

tree_icon_3 = get_tree_icon(float(last_value_soil_sensor_3))

try:
    last_value_soil_sensor_4 = df_soil_moisture_4['value'].iloc[-1]
except IndexError:
    last_value_soil_sensor_4 = 31

tree_icon_4 = get_tree_icon(float(last_value_soil_sensor_4))

try:
    last_value_soil_sensor_5 = df_soil_moisture_5['value'].iloc[-1]
except IndexError:
    last_value_soil_sensor_5 = 31

tree_icon_5 = get_tree_icon(float(last_value_soil_sensor_5))

custom_icon_soil_sensor = {
    "iconUrl": "/assets/bodensensor.svg",
    "iconSize": [40, 40]  # adjust based on your SVG's size
}

custom_icon_weather_station = {
    "iconUrl": "/assets/wetterstation.svg",
    "iconSize": [40, 40]  # adjust based on your SVG's size
}

def create_soil_moisture_graph():

    # In order for the x axis to not be reliant on the time of the database:
    # - get the current time
    # - calculate the time 24 h ago
    now = datetime.now()
    twenty_four_hours_ago = now - timedelta(hours=24)

    # Hardcode x axis values for the line graph with humidity of the soil - remove later
    start_time = twenty_four_hours_ago
    end_time = now
    x_values = [start_time + timedelta(hours=i) for i in range(25)]

    print(x_values)

    # Hardcode y axis values with 120 random values from 21 to 26 - remove later
    def random_y_values():
        y_values = [random.uniform(23, 26) for _ in range(25)]
        return y_values

    # #checks which of the sensors has the highest y-value, so that the green background color can be adjusted
    # global_y_max = max(
    #     float(df_soil_moisture_1['value'].max()),
    #     float(df_soil_moisture_2['value'].max()),
    #     float(df_soil_moisture_3['value'].max()),
    #     float(df_soil_moisture_4['value'].max()),
    #     float(df_soil_moisture_5['value'].max())
    # ) + 5

    max_precipitation = df_weatherstation_precipitation['value'].max() + 0.5

    # This trace is for the background red color from 0-10%
    trace_red = {
        'type': 'scatter',
        'x': [x_values[0], x_values[-1]],
        'y': [10, 10],
        'fill': 'tozeroy',
        'fillcolor': 'rgba(255, 0, 0, 0.3)',  # 50% transparent red
        'line': {'width': 0},
        'showlegend': False,
        'hoverinfo': 'none'
    }

    # This trace is for the background yellow color from 10-20%
    trace_yellow = {
        'type': 'scatter',
        'x': [x_values[0], x_values[-1]],
        'y': [20, 20],
        'fill': 'tonexty',
        'fillcolor': 'rgba(255, 255, 0, 0.3)',  # 50% transparent yellow
        'line': {'width': 0},
        'showlegend': False,
        'hoverinfo': 'none'
    }

    # Determine the maximum Y value to ensure the green trace covers the entire relevant region.
    try:
        # Find the max value in each dataframe's 'value' column
        max_values = [
            df_soil_moisture_1['value'].max(),
            df_soil_moisture_2['value'].max(),
            df_soil_moisture_3['value'].max(),
            df_soil_moisture_4['value'].max(),
            df_soil_moisture_5['value'].max()
        ]
        # Filter out None values in case any dataframe is empty
        max_values = [value for value in max_values if value is not None]

        # Find the highest max value among all dataframes
        y_max = max(max_values) if max_values else 50
    except ValueError:  # Handle the case where all 'value' columns are empty
        y_max = 50

    # This trace is for the background green color from 15% to y_max
    trace_green = {
        'type': 'scatter',
        'x': [x_values[0], x_values[-1]],
        'y': [float(y_max)+5, float(y_max)+5],
        'fill': 'tonexty',
        'fillcolor': 'rgba(0, 255, 0, 0.3)',  # 50% transparent green
        'line': {'width': 0},
        'showlegend': False,
        'hoverinfo': 'none'
    }

    # Find the earliest and latest times from all your data traces

    earliest_time = min(df_soil_moisture_1['time'])
    latest_time = max(df_soil_moisture_1['time'])

    # Update the x values for the background traces to cover the full range
    trace_red['x'] = [earliest_time, latest_time]
    trace_yellow['x'] = [earliest_time, latest_time]
    trace_green['x'] = [earliest_time, latest_time]


    trace_temp_1 = {
        'x': df_soil_moisture_1['time'],
        'y': df_soil_moisture_1['value'],
        'type': 'line',
        'name': 'Pleiner Mostbirne',
        'line': {
            'color': '#0000FF',  # Blue
            'width': 4
        },
        'showlegend': False,
        'hoverlabel': {
            'namelength': -1  # Shows the full name, regardless of length
        }
    }

    trace_temp_2 = {
         'x': df_soil_moisture_2['time'],
         'y': df_soil_moisture_2['value'],
        #'x': x_values,
        #'y': random_y_values(),
        'type': 'line',
        'name': 'Schöner von Nordhausen',
        'line': {
            'color': '#FF00FF',  # Magenta
            'width': 4
        },
        'showlegend': False,
        'hoverlabel': {
            'namelength': -1  # Shows the full name, regardless of length
        }
    }

    trace_temp_3 = {
         'x': df_soil_moisture_3['time'],
         'y': df_soil_moisture_3['value'],
        #'x': x_values,
        #'y': random_y_values(),
        'type': 'line',
        'name': 'Roter Boskoop',
        'line': {
            'color': '#00FFFF',  # Cyan
            'width': 4
        },
        'showlegend': False,
        'hoverlabel': {
            'namelength': -1  # Shows the full name, regardless of length
        }
    }

    trace_temp_4 = {
         'x': df_soil_moisture_4['time'],
         'y': df_soil_moisture_4['value'],
        #'x': x_values,
        #'y': random_y_values(),
        'type': 'line',
        'name': 'Cox Orangenrenette',
        'line': {
            'color': '#FFA500',  # Orange
            'width': 4
        },
        'showlegend': False,
        'hoverlabel': {
            'namelength': -1  # Shows the full name, regardless of length
        }
    }

    trace_temp_5 = {
         'x': df_soil_moisture_5['time'],
         'y': df_soil_moisture_5['value'],
        #'x': x_values,
        #'y': random_y_values(),
        'type': 'line',
        'name': 'Jonathan',
        'line': {
            'color': '#800080',  # Purple
            'width': 4
        },
        'showlegend': False,
        'hoverlabel': {
            'namelength': -1  # Shows the full name, regardless of length
        }
    }

    # Create a trace for precipitation
    trace_precipitation = {
        'x': df_weatherstation_precipitation['time'],
        'y': df_weatherstation_precipitation['value'],
        'type': 'bar',
        'name': 'Niederschlag',
        'marker': {'color': 'green'},  # Adjust the opacity to make it fully visible
        'hoverlabel': {'namelength': -1},  # Show the full name
        'yaxis': 'y2',  # Associate this trace with the secondary y-axis
        'showlegend': False  # Hide the legend for this trace

    }

    return dcc.Graph(
        figure={
            'data': [trace_red, trace_yellow, trace_green, trace_precipitation, trace_temp_1, trace_temp_2, trace_temp_3, trace_temp_4,
                     trace_temp_5],
            'layout': {
                'font': {'family': 'Poppins'},
                'title': 'Bodenfeuchte und Niederschlag<br>- letzte 24 Stunden',
                'autosize': True,
                'paper_bgcolor': 'rgba(0,0,0,0)',
                'width': '100%',
                'margin': {
                    'l': 40,  # Left margin
                    'r': 40,  # Right margin
                    'b': 80,  # Bottom margin
                    't': 40,  # Top margin
                },
                'xaxis': {
                    'fixedrange': True,  # Make the x-axis fixed for both graphs
                    'domain': [0, 1],  # Specify the x-axis domain to be shared
                    'range': [earliest_time, latest_time]
                },                'yaxis': {
                    'title': {
                        'text': 'Bodenfeuchte [%]',
                        'standoff': 20,
                        'rotate': 0
                    },
                    'overlaying': 'y2',
                    'fixedrange': True
                },
                'yaxis2': {
                    'title': 'Niederschlag [mm/h]',
                    'side': 'right',
                    'showgrid': False,
                    'range': [0, max_precipitation]  # Set the range to include the added 0.5 mm

                },

            },
        },
        config={'displayModeBar': False, 'staticPlot': False},
        style={'height': '100%', 'width': '100%'},
    )


def tree_layout():
    return html.Div([
        # Project Description
        dbc.Row(
            [
                dbc.Col(html.H1("Welche Bäume müssen bewässert werden?", id="bodenfeuchte", className="text-center mt-5 mb-5"), width=12),
            ]
        ),
        # Soil Moisture and Map
        dbc.Row(
            [                  # Text
                dbc.Col(html.Div(children=[
                    html.P("Die Farben zeigen uns, welche Bäume Wasser benötigen:"),
                    html.Div([
                        html.Div([
                            html.Img(src=green_tree["iconUrl"], style={"width": "40px", "height": "40px"}),
                            html.Span(" der Baum hat genügend Wasser", className="ms-2")
                        ], className="legend-item d-flex align-items-center"),
                        html.Div([
                            html.Img(src=yellow_tree["iconUrl"], style={"width": "40px", "height": "40px"}),
                            html.Span(" der Baum muss zeitnah bewässert werden", className="ms-2")
                        ], className="legend-item d-flex align-items-center"),
                        html.Div([
                            html.Img(src=red_tree["iconUrl"], style={"width": "40px", "height": "40px"}),
                            html.Span(" der Baum braucht dringend Wasser", className="ms-2")
                        ], className="legend-item d-flex align-items-center"),
                    ]),
                ], ), width=4, xs=12, sm=12, md=12, lg=6, xl=4, className='p-5'),
                # Map
                dbc.Col(html.Div(children=[
                    dl.Map([
                        dl.TileLayer(),
                        dl.Marker(position=[49.55733911301222, 7.3607157322857075], icon=tree_icon_1,
                                  children=[dl.Tooltip("Pleiner Mostbirne")]),
                        dl.Marker(position=[49.55751276556591, 7.361085800771698], icon=tree_icon_2,
                                  children=[dl.Tooltip("Schöner von Nordhausen")]),
                        dl.Marker(position=[49.55765249375624, 7.361099770403598], icon=tree_icon_3,
                                  children=[dl.Tooltip("Roter Boskoop")]),
                        dl.Marker(position=[49.55763383926781, 7.36134283963924], icon=tree_icon_4,
                                  children=[dl.Tooltip("Cox Orangenrenette")]),
                        dl.Marker(position=[49.55780646950395, 7.361366709398196], icon=tree_icon_5,
                                  children=[dl.Tooltip("Jonathan")]),
                    ],
                        className='leaflet-container',
                        style={'max-width': '100%'},
                        center=(49.557488461793795, 7.36099355082976),
                        zoom=18,
                        zoomControl=True,
                        dragging=False,
                        doubleClickZoom=False,
                        scrollWheelZoom=False,
                    ),
                ]), className="p-5", width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),

            ],
            className="", justify="center"),
        dbc.Row(  # Row for the soil moisture graph
            [
                dbc.Col(
                    create_soil_moisture_graph(),
                    width=12, xs=12, sm=12, md=10, lg=10, xl=10,
                ),
            ],
            className='mt-5 mb-5 ',
            justify='center',
        ),
        #row for the legend
        dbc.Row([  # Parent Row
            dbc.Col([  # Parent Column with width of 10
                dbc.Row([  # Nested Row
                    dbc.Col(  # First legend item
                        html.Div([
                            html.Div(style={"width": "40px", "borderBottom": "5px solid #0000FF"}), # Blue
                            html.Span("  Pleiner Mostbirne", className="ms-4")
                        ], className="legend-item d-flex align-items-center ms-5"),
                        xs=12, sm=12, md=12, lg=12, xl=12
                    ),
                    dbc.Col(  # Second legend item
                        html.Div([
                            html.Div(style={"width": "40px", "borderBottom": "5px solid #FF00FF"}),  # Magenta
                            html.Span("  Schöner von Nordhausen", className="ms-4")
                        ], className="legend-item d-flex align-items-center ms-5"),
                        xs=12, sm=12, md=12, lg=12, xl=12
                    ),
                    dbc.Col(  # Third legend item
                        html.Div([
                            html.Div(style={"width": "40px", "borderBottom": "5px solid #00FFFF"}),  # Cyan line
                            html.Span("  Roter Boskoop", className="ms-4")
                        ], className="legend-item d-flex align-items-center ms-5"),
                        xs=12, sm=12, md=12, lg=12, xl=12
                    ),
                    dbc.Col(  # Fourth legend item
                        html.Div([
                            html.Div(style={"width": "40px", "borderBottom": "5px solid #FFA500"}),  # orange line
                            html.Span("  Cox Orangenrenette", className="ms-4")
                        ], className="legend-item d-flex align-items-center ms-5"),
                        xs=12, sm=12, md=12, lg=12, xl=12
                    ),
                    dbc.Col(  # Fifth legend item
                        html.Div([
                            html.Div(style={"width": "40px", "borderBottom": "5px solid #800080"}),  # purple line
                            html.Span("  Jonathan", className="ms-4")
                        ], className="legend-item d-flex align-items-center ms-5"),
                        xs=12, sm=12, md=12, lg=12, xl=12
                    ),
                ], className='d-flex'),
            ], width=12, xs=12, sm=12, md=10, lg=10, xl=10),  # Parent column with width of 10 for md and larger screens
        ], className="mb-5", justify='center')

    ])
