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


def hintergrund_section():
    return html.Div([
        # Project Description
        dbc.Row([
            dbc.Col(html.H1("Hintergrund der Fläche", id="hintergrund", className="text-center mt-5"), width=12)
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(dcc.Markdown("""
        Im Rahmen der „Klimafitchallenge“ der Kreisverwaltung Kusel im Jahr 2021 wurde mit 
        Unterstützung der Kreissparkasse Kusel in direkter Nähe zur Burg Lichtenberg eine 
        Streuobstwiese mit 15 Bäumen angepflanzt. Durch umweltbewusstesVerhalten konnten die Mitarbeitenden
        jede Menge Punkte sammeln und so 1,2 Tonnen CO2 einsparen. Am Ende der Aktion wurden 
        die Punkte aller Mitarbeitenden gegen 15 Obstbäume eingetauscht, die im Frühjahr 2022 
        eingepflanzt wurden. Die Schüler und Schülerinnen der BBS Kusel schenkten der Fläche in 
        Zusammenarbeit mit dem TRAFO-Projekt des Landkreises zudem zwei selbstgebaute Insektenhotels 
        in Form von Musikinstrumenten – passend zum Kuseler Wandermusikantenland. Seit September 2023 
        ist die Fläche neben den längeren (Premium-)Wanderwegen auch Teil eines eigens dafür angelegten 
        und 3,2 Kilometer langen Streuobstwiesenwanderweges.
                """, className="text-black m-5", style={"lineHeight": "250%", })),
                lg=6, md=12, sm=12, width=4, xl=4, xs=12
            ),
            dbc.Col(
                html.Div(html.Img(src="/assets/lorawan.png", className="img-fluid rounded mx-auto d-block w-75 mt-5",
                                  alt="Responsive image")),
                lg=6, md=12, sm=12, width=4, xl=4, xs=12
            )
        ], className="", justify="center"),
    ]
    )
