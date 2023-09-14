from dash import html
import dash_bootstrap_components as dbc

def jumbotron():
    jumbotron_content = dbc.Col(
        html.Div(
            [
                html.H2([
                    "Sensorikfläche an der",
                    html.Br(),  # This introduces a line break
                    "Burg Lichtenberg"
                ],
                className="display-3",  style={'color': 'white'}),
                html.Hr(className="my-2 border-5", style={'color': 'white'}),
                html.P(
                    "Welche (teilweise) versteckten Prozesse spielen sich auf einer Streuobstwiese im Boden,"
                    " den Bäumen oder auch deren Umwelt ab? Dies wird auf der ersten Sensorik-Experimentierfläche"
                    " im Landkreis Kusel erforscht.", className="lead", style={'color': 'white'}
                ),
                dbc.Button("Sanfter Einstieg", color="primary", className="btn-lg me-2",
                           style={'backgroundColor': 'white', 'borderColor': 'white', 'color': 'black'}),
                dbc.Button("Tiefer eintauchen", className="btn-lg",
                           style={'backgroundColor': 'white', 'borderColor': 'white', 'color': 'black'}),
            ],
            className="h-100 p-5",
        ),
        md=6,
    )

    return dbc.Row(
        [jumbotron_content],
        className="align-items-md-stretch",
    )
