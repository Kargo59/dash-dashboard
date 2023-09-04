import dash
from dash import dcc
from dash import html
import dash_leaflet as dl
import numpy as np
import dash_bootstrap_components as dbc
import requests


app = dash.Dash(__name__, meta_tags=[
        {'name': 'viewport', 'content': 'width=device-width, initial-scale=1, maximum-scale=1.2, minimum-scale=0.5'}],
        external_stylesheets=[dbc.themes.SANDSTONE, "/assets/style.css"], )

app.title = "Sensornetz Smart City"

# Generate a sequence of a hundred data points for the line chart
x_values = np.linspace(1, 10, 100)
y_values = np.sin(x_values) + np.random.randn(100)  # Adding some randomness to the data


def set_alert_color():
    try:
        data_url = 'https://api.agify.io/?name=meelad'  # API URL
        response = requests.get(data_url)
        api_data = response.json()
        print(api_data)
        age = api_data.get('age', 0)  # Get the 'age' value from the API response (default to 0 if not found)

        # Set the color based on the age value
        if age == 33:
            return 'green'  # Change to green if age is 33
        else:
            return 'primary'  # Change to blue for other ages
    except Exception as e:
        print(f"Error fetching data from the API: {e}")
        return 'info'  # Return a default color in case of an error

app.layout = dbc.Container(children=[
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="http://127.0.0.1:8050#top")),
            #store these in a config file!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            dbc.NavItem(dbc.NavLink("Über das Projekt", href="http://127.0.0.1:8050#projektbeschreibung")),
            dbc.NavItem(dbc.NavLink("Wetterdaten", href="http://127.0.0.1:8050#wetterdaten")),
            dbc.NavItem(dbc.NavLink("Bodenfeuchte", href="http://127.0.0.1:8050#bodenfeuchte")),
        ],
        brand="Sensornetz Land Lieben",
        brand_href="#",
        color="primary",
        dark=True,
    className="sticky-top"),
    # first container for the tile and the background thats going to be paralaxxed
    html.Div(className="parallax-container", id='top'),
    # second container, right underneath the title and parallax image
    html.Div(
        [
            # header
            dbc.Row(dbc.Col(html.H1("Über das Projekt", className="text-center p-5",  id="projektbeschreibung"), width=12), ),
            # rest
            dbc.Row(
                [
                    dbc.Col(html.Div(children=[
                        html.Img(src='/assets/main2.jpg', className='img-fluid rounded mx-auto d-block m-5 px-5',
                                 alt="Responsive image",) ,
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
            dbc.Row(dbc.Col(html.H1("Wetterdaten", className="text-center p-5", id="wetterdaten"), width=12),),
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
                            className="text-black bg-white rounded m-5",),
                    ],), width=4, xs=12, sm=12, md=12, lg=4, xl=4,),
                dbc.Col(html.Div(children=[
                    dbc.Row(
                        dcc.Graph(
                        figure={
                            'data': [
                                {'x': x_values, 'y': y_values, 'type': 'line', 'name': 'Data 4'},
                            ],
                            'layout': {
                                'title': 'Temperatur der letzten 24 Stunden',
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
                                    'title': 'Niederschlag der letzten 24 Stunden',
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
            dbc.Row(dbc.Col(html.H1("Optimierte Bewässerung", className="text-center p-5", id="bodenfeuchte"), width=12), ),
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
                dbc.Col(html.H1("Aktuelle Bedingungen", className="text-center"), width=12),  # New column with H1 title
            ),
            dbc.Row(
                    [dbc.Col(html.Div([
                        html.Img(src='/assets/tree.svg', className='img-fluid rounded-circle mx-auto d-block m-5 icon-responsive',
                         alt="Responsive image", style={'background-color': "#86eb34"}),
                        dcc.Markdown('''
                            **Baum 1**
                        ''', className="text-center")
                        ,
                ]), width=4, xs=4, sm=4, md=4, lg=2, xl=2),
                    dbc.Col(html.Div([
                        html.Img(src='/assets/tree.svg', className='img-fluid rounded-circle mx-auto d-block m-5 icon-responsive',
                         alt="Responsive image", style={'background-color': "#f4fc03"}),
                        dcc.Markdown('''
                            **Baum 2**
                            ''', className="text-center"
                                     )
            ]), width=4, xs=4, sm=4, md=4, lg=2, xl=2),
                    dbc.Col(html.Div([
                        html.Img(src='/assets/tree.svg', className='img-fluid rounded-circle mx-auto d-block m-5 icon-responsive',
                         alt="Responsive image", style={'background-color': "#fc0303"}),
                        dcc.Markdown('''
    **Baum 3**
    ''', className="text-center"
                                     )
            ]), width=4, xs=4, sm=4, md=4, lg=2, xl=2),],justify='center', className='m-5'),
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
