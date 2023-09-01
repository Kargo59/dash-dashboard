import dash
from dash import dcc
from dash import html
import dash_leaflet as dl
import numpy as np
import dash_bootstrap_components as dbc
import json

app = dash.Dash(__name__, meta_tags=[
        {'name': 'viewport', 'content': 'width=device-width, initial-scale=1, maximum-scale=1.2, minimum-scale=0.5'}],
        external_stylesheets=[dbc.themes.SANDSTONE, "/assets/style.css"], )

app.title = "Sensornetz Smart City"

# Generate a sequence of a hundred data points for the line chart
x_values = np.linspace(1, 10, 100)
y_values = np.sin(x_values) + np.random.randn(100)  # Adding some randomness to the data




app.layout = dbc.Container(children=[
    # first container for the tile and the background thats going to be paralaxxed
    html.Div(className="parallax-container",),
    # second container, right underneath the title and parallax image
    html.Div(
        [
            # header
            dbc.Row(dbc.Col(html.H1("Über das Projekt", className="text-center p-5",), width=12), ),
            # rest
            dbc.Row(
                [
                    dbc.Col(html.Div(children=[
                        html.Img(src='/assets/main2.jpg', className='img-fluid rounded mx-auto d-block m-5 px-5',
                                 alt="Responsive image", ) ,
                    ]), width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),
                    dbc.Col(html.Div(children=[
                        dcc.Markdown(
                            """
                            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                            when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
                            and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                            \n\n 
                            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                            when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
                            and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                            """
                            ,
                            className="text-black bg-white rounded m-5",),
                    ], ), width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),
                ],
                className="", justify="center"),
        ]
    ),
    # third container for the weather data
    html.Div(
        [
            # header
            dbc.Row(dbc.Col(html.H1("Wetterdaten", className="text-center p-5"), width=12),),
            # rest
            dbc.Row(
                [dbc.Col(html.Div(children=[
                        dcc.Markdown(
                            """
                            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                            when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
                            and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                            \n\n 
                            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                            when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
                            and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                            """
                            ,
                            className="text-black bg-white rounded m-5", ),
                    ],), width=4, xs=12, sm=12, md=12, lg=4, xl=4,),
                dbc.Col(html.Div(children=[
                    dbc.Row(
                        dcc.Graph(
                        figure={
                            'data': [
                                {'x': x_values, 'y': y_values, 'type': 'line', 'name': 'Data 4'},
                            ],
                            'layout': {
                                'title': 'Temperatur der letzten 7 Tage',
                                'paper_bgcolor': 'rgba(0,0,0,0)',
                                'width': '100%',
                            }
                        },
                    ),),
                    dbc.Row(
                        dcc.Graph(
                            figure={
                                'data': [
                                    {'x': x_values, 'y': y_values, 'type': 'line', 'name': 'Data 4',
                                     'line': {'color': 'red'},
                                     },
                                ],
                                'layout': {
                                    'title': 'Niederschlag der letzten 7 Tage',
                                    'paper_bgcolor': 'rgba(0,0,0,0)',
                                    'width': '100%',
                                }
                            },
                        ),),

                    ]), width=4, xs=12, sm=12, md=12, lg=4, xl=4, ),
                ],
            className="", justify="center"),
        ]
    ),
    # fourth container, for the soil moisture data
    html.Div(
        [
            # header
            dbc.Row(dbc.Col(html.H1("Optimierte Bewässerung", className="text-center p-5"), width=12), ),
            # rest
            dbc.Row(
                [
                    dbc.Col(html.Div(children=[
                        dl.Map([
                            dl.TileLayer(),
                            dl.Marker(
                                position=[49.557938, 7.361618],
                                children=[
                                    dl.Tooltip("Bodenfeuchtesensor 1")
                                ]
                            ),
                            dl.Marker(
                                position=[49.558005, 7.361978],
                                children=[
                                    dl.Tooltip("Bodenfeuchtesensor 2")
                                ]
                            ),
                            dl.Marker(
                                position=[49.558240, 7.362581],
                                children=[
                                    dl.Tooltip("Bodenfeuchtesensor 3")
                                ]
                            ),
                            dl.Marker(
                                position=[49.558573, 7.363353],
                                children=[
                                    dl.Tooltip("Bodenfeuchtesensor 4")
                                ]
                            ),
                            dl.Marker(
                                position=[49.558544, 7.363788],
                                children=[
                                    dl.Tooltip("Bodenfeuchtesensor 5")
                                ]
                            ),
                            dl.Marker(
                                position=[49.558357, 7.363165],
                                children=[
                                    dl.Tooltip("Wetterstation")
                                ]
                            )
                        ],
                            className='leaflet-container',
                            style={'max-width': '100%'},
                            center=(49.556846, 7.358865),
                            zoom=16
                        ),
                    ]),className="p-5", width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),
                    dbc.Col(html.Div(children=[
                        dcc.Markdown(
                            """
                            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                            when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
                            and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                            \n\n 
                            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                            when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
                            and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                            """
                            ,
                            className="text-black bg-white rounded p-5", ),

                    ], ), width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),
                ],
                className="", justify="center"),
            dbc.Row(
                dbc.Row(
                    [
                        dbc.Col(html.Div([
                            html.H3("Aktuelle Bedingungen:", className="text-center p-3"),
                            dbc.Alert("This is a success alert! Well done!", color="success"),
                            dbc.Alert("This is a warning alert... be careful...", color="warning"),
                            dbc.Alert("This is a danger alert. Scary!", color="danger"),

                        ]),
                            width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),
                        dbc.Col(html.Div(children=[
                            dcc.Markdown(
                                """
                                
                                """
                                ,
                                className="text-black bg-white rounded m-5", ),
                        ], ), width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),
                    ],
                    className="", justify="center"), ),
        ]
    ),
],


fluid=True)




@app.server.route('/data')
def etl():
    # Your code to execute when the endpoint is accessed
    return "Hello from your endpoint!"

if __name__ == '__main__':
    app.run_server(debug=True)
