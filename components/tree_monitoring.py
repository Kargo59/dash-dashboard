import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_leaflet as dl
from data_source import fetch_soil_water_1, fetch_soil_water_2, fetch_soil_water_3, fetch_soil_water_4, fetch_soil_water_5

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

last_value_soil_sensor_1 = df_soil_moisture_1['value'].iloc[-1]
tree_icon_1 = get_tree_icon(float(last_value_soil_sensor_1))

last_value_soil_sensor_2 = df_soil_moisture_2['value'].iloc[-1]
tree_icon_2 = get_tree_icon(float(last_value_soil_sensor_2))

last_value_soil_sensor_3 = df_soil_moisture_3['value'].iloc[-1]
tree_icon_3 = get_tree_icon(float(last_value_soil_sensor_3))

last_value_soil_sensor_4 = df_soil_moisture_4['value'].iloc[-1]
tree_icon_4 = get_tree_icon(float(last_value_soil_sensor_4))

last_value_soil_sensor_5 = df_soil_moisture_5['value'].iloc[-1]
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
    #checks which of the sensors has the highest y-value, so that the green background color can be adjusted
    global_y_max = max(
        float(df_soil_moisture_1['value'].max()),
        float(df_soil_moisture_2['value'].max()),
        float(df_soil_moisture_3['value'].max()),
        float(df_soil_moisture_4['value'].max()),
        float(df_soil_moisture_5['value'].max())
    ) + 5

    # This trace is for the background red color from 0-5%
    trace_red = {
        'type': 'scatter',
        'x': [df_soil_moisture_1['time'].iloc[0], df_soil_moisture_1['time'].iloc[-1]],
        'y': [10, 10],
        'fill': 'tozeroy',
        'fillcolor': 'rgba(255, 0, 0, 0.3)',  # 50% transparent red
        'line': {'width': 0},
        'showlegend': False,
        'hoverinfo': 'none'
    }

    # This trace is for the background yellow color from 5-15%
    trace_yellow = {
        'type': 'scatter',
        'x': [df_soil_moisture_1['time'].iloc[0], df_soil_moisture_1['time'].iloc[-1]],
        'y': [20, 20],
        'fill': 'tonexty',
        'fillcolor': 'rgba(255, 255, 0, 0.3)',  # 50% transparent yellow
        'line': {'width': 0},
        'showlegend': False,
        'hoverinfo': 'none'
    }

    # Determine the maximum Y value to ensure the green trace covers the entire relevant region.
    y_max = max(df_soil_moisture_1['value'])

    # This trace is for the background green color from 15% to y_max
    trace_green = {
        'type': 'scatter',
        'x': [df_soil_moisture_1['time'].iloc[0], df_soil_moisture_1['time'].iloc[-1]],  # This assumes all datasets share the same time range.
        'y': [global_y_max, global_y_max],
        'fill': 'tonexty',
        'fillcolor': 'rgba(0, 255, 0, 0.3)',  # 50% transparent green
        'line': {'width': 0},
        'showlegend': False,
        'hoverinfo': 'none'
    }

    trace_temp_1 = {
        'x': df_soil_moisture_1['time'],
        'y': df_soil_moisture_1['value'],
        'type': 'line',
        'name': 'Temperature 1',
        'line': {
            'color': '#0000FF',  # Blue
            'width': 4
        },
        'showlegend': False
    }

    trace_temp_2 = {
        'x': df_soil_moisture_2['time'],
        'y': df_soil_moisture_2['value'],
        'type': 'line',
        'name': 'Temperature 2',
        'line': {
            'color': '#FF00FF',  # Magenta
            'width': 4
        },
        'showlegend': False
    }

    trace_temp_3 = {
        'x': df_soil_moisture_3['time'],
        'y': df_soil_moisture_3['value'],
        'type': 'line',
        'name': 'Temperature 3',
        'line': {
            'color': '#00FFFF',  # Cyan
            'width': 4
        },
        'showlegend': False
    }

    trace_temp_4 = {
        'x': df_soil_moisture_4['time'],
        'y': df_soil_moisture_4['value'],
        'type': 'line',
        'name': 'Temperature 4',
        'line': {
            'color': '#FFA500',  # Orange
            'width': 4
        },
        'showlegend': False
    }

    trace_temp_5 = {
        'x': df_soil_moisture_5['time'],
        'y': df_soil_moisture_5['value'],
        'type': 'line',
        'name': 'Temperature 5',
        'line': {
            'color': '#800080',  # Purple
            'width': 4
        },
        'showlegend': False
    }

    return dcc.Graph(
        figure={
            'data': [trace_red, trace_yellow, trace_green, trace_temp_1, trace_temp_2, trace_temp_3, trace_temp_4, trace_temp_5],
            'layout': {
                'font': {
                    'family': 'Poppins',
                },
                'title': 'Bodenfeuchte der letzten 24 Stunden',
                'autosize': True,
                'paper_bgcolor': 'rgba(0,0,0,0)',
                'width': '100%',
                'xaxis': {'fixedrange': True},
                                'yaxis': {
                    'title': {
                        'text': 'Bodenfeuchte [%]',
                        'standoff': 20,
                        'rotate': 0},
                    'fixedrange': True,},
                'margin': {
                    'l': 40,  # Left margin
                    'r': 40,  # Right margin
                    'b': 40,  # Bottom margin
                    't': 40,  # Top margin
                },
            }
        },
        config={'displayModeBar': False, 'staticPlot': True},
        style={'height': '100%', 'width': '100%'},
    )


def tree_layout():
    return html.Div([
        # Project Description
        dbc.Row(
            [
                dbc.Col(html.H1("Welche Bäume müssen bewässert werden?", className="text-center mt-5 mb-5"), width=12),
            ]
        ),
        # Soil Moisture and Map
        dbc.Row(
            [                  # Text
                dbc.Col(html.Div(children=[
                    dcc.Markdown(
                        """
                        Die ersten fünf Sensoren die im September 2023 auf der Fläche einziehen durften sollen 
                        unter anderem durch die Messung der Bodenfeuchtigkeit die Pflege und Bewässerung 
                        der Obstbäume erleichtern. Wir hoffen, dass die Obstbäume dadurch zu großen, 
                        schattenspendenden Bäumen heranwachsen können und ihr Bedarf nach Wasser und Düngemittel 
                        besser eingeschätzt werden kann.  

                        """
                        ,
                        className="text-black bg-white rounded p-5", style={"lineHeight": "250%", }),
                ], ), width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),
                # Map
                dbc.Col(html.Div(children=[
                    dl.Map([
                        dl.TileLayer(),
                        dl.Marker(position=[49.55733911301222, 7.3607157322857075], icon=tree_icon_1,
                                  children=[dl.Tooltip("Baum 1")]),
                        dl.Marker(position=[49.55751276556591, 7.361085800771698], icon=tree_icon_2,
                                  children=[dl.Tooltip("Baum 2")]),
                        dl.Marker(position=[49.55765249375624, 7.361099770403598], icon=tree_icon_3,
                                  children=[dl.Tooltip("Baum 3")]),
                        dl.Marker(position=[49.55763383926781, 7.36134283963924], icon=tree_icon_4,
                                  children=[dl.Tooltip("Baum 4")]),
                        dl.Marker(position=[49.55780646950395, 7.361366709398196], icon=tree_icon_5,
                                  children=[dl.Tooltip("Baum 5")]),
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
                    # Legend (Below Map)
                    dbc.Col(html.Div([
                        html.Div([
                            html.Img(src=green_tree["iconUrl"], style={"width": "40px", "height": "40px"}),
                            html.Span(" - der Baum hat genügend Wasser", className="ml-2")
                        ], className="legend-item d-flex align-items-center"),
                        html.Div([
                            html.Img(src=yellow_tree["iconUrl"], style={"width": "40px", "height": "40px"}),
                            html.Span(" - bald ist Bewässern angesagt", className="ml-2")
                        ], className="legend-item d-flex align-items-center"),
                        html.Div([
                            html.Img(src=red_tree["iconUrl"], style={"width": "40px", "height": "40px"}),
                            html.Span(" - der Baum braucht dringend Wasser", className="ml-2")
                        ], className="legend-item d-flex align-items-center"),
                    ]), )

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
                            html.Div(style={"width": "40px", "borderBottom": "5px solid #1f77b4"}),  # blue line
                            html.Span(" - Sensor 1 Data", className="ml-2")
                        ], className="legend-item d-flex justify-content-center align-items-center"),
                        xs=12, sm=12, md=2, lg=2, xl=2
                    ),
                    dbc.Col(  # Second legend item
                        html.Div([
                            html.Div(style={"width": "40px", "borderBottom": "5px solid #ff7f0e"}),  # orange line
                            html.Span(" - Sensor 2 Data", className="ml-2")
                        ], className="legend-item d-flex justify-content-center align-items-center"),
                        xs=12, sm=12, md=2, lg=2, xl=2
                    ),
                    dbc.Col(  # Third legend item
                        html.Div([
                            html.Div(style={"width": "40px", "borderBottom": "5px solid #2ca02c"}),  # green line
                            html.Span(" - Sensor 3 Data", className="ml-2")
                        ], className="legend-item d-flex justify-content-center align-items-center"),
                        xs=12, sm=12, md=2, lg=2, xl=2
                    ),
                    dbc.Col(  # Fourth legend item
                        html.Div([
                            html.Div(style={"width": "40px", "borderBottom": "5px solid #d62728"}),  # red line
                            html.Span(" - Sensor 4 Data", className="ml-2")
                        ], className="legend-item d-flex justify-content-center align-items-center"),
                        xs=12, sm=12, md=2, lg=2, xl=2
                    ),
                    dbc.Col(  # Fifth legend item
                        html.Div([
                            html.Div(style={"width": "40px", "borderBottom": "5px solid #9467bd"}),  # purple line
                            html.Span(" - Sensor 5 Data", className="ml-2")
                        ], className="legend-item d-flex justify-content-center align-items-center"),
                        xs=12, sm=12, md=2, lg=2, xl=2
                    ),
                ], className='d-flex justify-content-center'),
            ], width=12, xs=12, sm=12, md=10, lg=10, xl=10),  # Parent column with width of 10 for md and larger screens
        ], className="mb-5", justify='center')

    ])
