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

def soil_moisture_layout():
    return     html.Div(
        [
            # header
            dbc.Row(dbc.Col(html.H1("Bodenfeuchte und optimierte Bewässerung", className="text-center p-5", id="bodenfeuchte"), width=12), ),
            # rest
            dbc.Row(
                [
                    dbc.Col(html.Div(children=[
                        dl.Map([
                            dl.TileLayer(),
                            dl.Marker(
                                position=[49.557938, 7.361618],
                                icon=custom_icon_soil_sensor,
                                children=[
                                    dl.Tooltip("Bodenfeuchtesensor 1"),
                                ]
                            ),
                            dl.Marker(
                                position=[49.558005, 7.361978],
                                icon=custom_icon_soil_sensor,
                                children=[
                                    dl.Tooltip("Bodenfeuchtesensor 2")
                                ]
                            ),
                            dl.Marker(
                                position=[49.558240, 7.362581],
                                icon=custom_icon_soil_sensor,
                                children=[
                                    dl.Tooltip("Bodenfeuchtesensor 3")
                                ]
                            ),
                            dl.Marker(
                                position=[49.558573, 7.363353],
                                icon=custom_icon_soil_sensor,
                                children=[
                                    dl.Tooltip("Bodenfeuchtesensor 4")
                                ]
                            ),
                            dl.Marker(
                                position=[49.558544, 7.363788],
                                icon=custom_icon_soil_sensor,
                                children=[
                                    dl.Tooltip("Bodenfeuchtesensor 5")
                                ]
                            ),
                            dl.Marker(
                                position=[49.558357, 7.363165],
                                icon=custom_icon_weather_station,
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
                             Die ersten fünf Sensoren die im September 2023 auf der Fläche einziehen durften sollen 
                             unter anderem durch die Messung der Bodenfeuchtigkeit die Pflege und Bewässerung der 
                             Obstbäume optimieren. Gemessen wird:
                            -	die Bodenfeuchte in Prozent. Diese ist für die Versorgung der Obstbäume mit ausreichend 
                            Wasser von hoher Bedeutung. Ist der Boden zu trocken, können keine Photosynthese und kein 
                            Baumwachstum stattfinden. Mithilfe der Sensoren soll nicht nur ein zu trockener Boden, 
                            sondern auch eine übermäßige Bewässerung verhindert und damit Wasser eingespart werden. 
                            Die Sensoren sind in 50 Zentimetern Tiefe angebracht. 
                            -	die Bodentemperatur in Grad Celsius. Unter 5 Grad Celsius sollte von einer Pflanzung 
                            abgesehen werden, unter 0 Grad Celsius spricht man von Bodenfrost.
                            -	Die elektrische Leitfähigkeit in Mikrosiemens pro Zentimeter gibt Aufschluss über den 
                            Nährstoffgehalt des Bodens und zeigt den Düngebedarf sowie die Bewässerung des Bodens an. 
                            Bei einem Wert unter 0,3 Mikrosiemens pro Zentimeter sollte der Boden gedüngt werden. Ein 
                            Wert von 0,8 Mikrosiemens pro Zentimeter deutet auf eine Überdüngung hin, was die Fähigkeit 
                            der Pflanzen Nährstoffe und Wasser aufzunehmen und damit auch das Wachstum hemmt. 
                            Wir hoffen, dass die Obstbäume auf der Streuobstwiese mithilfe der Bodenfeuchtesensoren zu 
                            großen, schattenspendenden Bäumen heranwachsen können und ihr Bedarf nach Wasser und 
                            Düngemittel besser eingeschätzt werden kann.  
                            """
                            ,
                            className="text-black bg-white rounded p-5", ),

                    ], ), width=4, xs=12, sm=12, md=12, lg=6, xl=4, ),
                ],
                className="", justify="center"),
            dbc.Row(
                dbc.Col(html.H1("Welche Bäume müssen bewässert werden?", className="text-center"), width=12),  # New column with H1 title
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
    )
