from dash import dcc, html
import dash_bootstrap_components as dbc


#create the second container, right underneath the title and parallax image
def project_description_section():
    return html.Div([
    dbc.Row([
        dbc.Col(
            html.H1("Über das Projekt", id="projektbeschreibung", className="text-center p-5"),
            width=12
        )
    ]),
    dbc.Row([
        dbc.Col(
            html.Div(
                html.Img(src="/assets/wanderweg_logo.png", className="img-fluid rounded mx-auto d-block m-5 px-5 w-75", alt="Responsive image")
            ),
            lg=6, md=12, sm=12, width=4, xl=4, xs=12
        ),
        dbc.Col(
            html.Div(
                dcc.Markdown("""
                Als Einstieg in das Projekt betrachten wir zunächst die Fläche an sich:
                - Streuobstwiese in direkter Nähe zur Burg Lichtenberg in Thallichtenberg(Direktlink zur Karte)
                - 15 Äpfel- und Birnenbäume, 2 Insektennistkästen, ein Infoschild zur Streuobstwiese und eine Liegebank
                - Fläche ist Teil mehrerer (Premium-)Wanderwege im Landkreis Kusel
                ...
                - Eine Wetterstation
                - Fünf Bodenfeuchtesensoren
                """, className="text-black bg-white rounded m-5")
            ),
            lg=6, md=12, sm=12, width=4, xl=4, xs=12
        )
    ], className="", justify="center")
])
