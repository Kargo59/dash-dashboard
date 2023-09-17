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
            dbc.Col(html.H1("Eingesetzte Technik", id="lorawan", className="text-center mt-5"), width=12)
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(html.Img(src="/assets/lorawan.png", className="img-fluid rounded mx-auto d-block w-75",
                                  alt="Responsive image")),
                lg=6, md=12, sm=12, width=4, xl=4, xs=12
            ),
            dbc.Col(
                html.Div(dcc.Markdown("""
                Als Einstieg in das Projekt betrachten wir zunächst die Fläche an sich:
                Streuobstwiese in direkter Nähe zur Burg Lichtenberg in Thallichtenberg
                15 Äpfel- und Birnenbäume, 2 Insektennistkästen, ein Infoschild zur Streuobstwiese und eine Liegebank
                Fläche ist Teil mehrerer (Premium-)Wanderwege im Landkreis Kusel
                Eine Wetterstation
                Fünf Bodenfeuchtesensoren
                """, className="text-black bg-white rounded m-5", style={"lineHeight":"200%", "font-style":"italic"})),
                lg=6, md=12, sm=12, width=4, xl=4, xs=12
            ),

        ], className="mt-5 mb-5", justify="center"),
    ]
    )
