from dash import html, dcc
import dash_bootstrap_components as dbc

def jumbotron():
    hero_content = dbc.Col(
        html.Div(
            [
                html.H2([
                    "Experimentierfläche an der",
                    html.Br(),  # This introduces a line break
                    "Burg Lichtenberg"
                ],
                    className='display-5',
                    style={'color': 'white', 'font-weight': '700'}),
                html.Hr(style={'borderTop': '3px solid white', 'width': '100%'}),
                html.P("Was ist denn auf der Obstwiese los?",
                       style={'color': 'white', 'font-weight': '500'}),
                html.A(
                    dbc.Button(
                        "Jetzt entdecken",
                        color="primary",
                        className="btn-lg me-2",
                        style={
                            'backgroundColor': 'white',
                            "width": "150px",
                            'borderColor': 'white',
                            'color': 'black',
                            'borderRadius': '0'
                        }
                    ),
                    href="#projektbeschreibung"
                ),
                html.A(
                    dbc.Button(
                        "Weitere Infos",
                        color="primary",
                        className="btn-lg me-2",
                        style={
                            'backgroundColor': 'white',
                            "width": "150px",
                            'borderColor': 'white',
                            'color': 'black',
                            'borderRadius': '0'
                        }
                    ),
                    href="#hintergrund"
                ),
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
