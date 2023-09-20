import dash_bootstrap_components as dbc
from dash import html, dcc

def footer():
    return html.Div([
        dbc.Row([
            dbc.Col(
                html.A("Impressum", href="/impressum", className="d-flex justify-content-center",
                       style={"text-decoration": "none", "color": "#000"}),
                width=6, lg=6, md=6, sm=12, xl=6, xs=12
            ),
            dbc.Col(
                html.A("Datenschutzbestimmungen", href="/datenschutzbestimmungen", className="d-flex justify-content-center",
                       style={"text-decoration": "none", "color": "#000"}),
                width=6, lg=6, md=6, sm=12, xl=6, xs=12
            ),
        ], className="justify-content-center mb-0", style={"margin-top":"100px"}),
    ])
