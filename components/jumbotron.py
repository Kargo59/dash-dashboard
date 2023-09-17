from dash import html, dcc
import dash_bootstrap_components as dbc

def jumbotron():
    hero_content = dbc.Col(
        html.Div(
            [
                html.H2([
                    "Sensorikfläche",
                    html.Br(),  # This introduces a line break
                    "Burg Lichtenberg"
                ],
                    className='display-5',
                    style={'color': 'white', 'font-weight': '700'}),
                dbc.Button("Zum Projekt", color="primary", className="btn-lg ",
                           style={'backgroundColor': 'white', 'borderColor': 'white', 'color': 'black', 'borderRadius': '0'}),
            ],
            className="",
        ),
        md=12,
        className="d-flex flex-row justify-content-center h-100 p-5",  # this centers content vertically
    )

    return dbc.Row(
        [hero_content],
        className="d-flex flex-row justify-content-center align-items-center h-100",
    )
