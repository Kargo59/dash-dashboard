import dash_bootstrap_components as dbc
from dash import html, dcc

def footer():
    return html.Div([
        dbc.Row([
            dbc.Col(
                html.P("Impressum", className="d-flex justify-content-center"),
                width=6, lg=6, md=6, sm=12, xl=6, xs=12
            ),
            dbc.Col(
                html.P("Datenschutzbestimmungen", className="d-flex justify-content-center"),
                width=6, lg=6, md=6, sm=12, xl=6, xs=12
            ),
        ], className="justify-content-center mb-0", style={"margin-top":"100px"}),
    ])
