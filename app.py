import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from components.jumbotron import jumbotron
from components.weather_station_section import create_temperature_graph, create_precipitation_graph, weather_text_content, weather_now_text_content, weather_data_layout
from components.project_description_section import project_description_section
from components.tech_description_section import tech_description_section
from components.soil_moisture_section import soil_moisture_layout
from components.tree_monitoring import tree_layout
from components.navbar import Navbar
from dash import Input, Output, State
from components.hintergrund_section import hintergrund_section
from components.footer import footer
from dash.dependencies import Input, Output
from pages.impressum import impressum_layout
from pages.datenschutz import datenschutz_layout


jumbotron = jumbotron()

app = dash.Dash(__name__, meta_tags=[
        {'name': 'viewport', 'content': 'width=device-width, initial-scale=1, maximum-scale=1.2, minimum-scale=0.5'}],
        external_stylesheets=[dbc.themes.SANDSTONE, "/assets/style.css"], )

app.title = "Sensornetz LAND L(i)EBEN"



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(Navbar(), id='navbar', style={"position": "sticky", "top":"0px" }, className="sticky-navbar sticky-top"),
    html.Div(id='page-content'),
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/impressum':
        return impressum_layout()
    elif pathname == '/datenschutzbestimmungen':
        return datenschutz_layout()
    else:
        return [
            html.Div([
                html.Div(jumbotron, className=""),
            ], className="parallax-container d-flex flex-row justify-content-center align-items-center", id='top'),
            #section "About the project"
            project_description_section(),
            # fifth container, for the tree monitoring
            tree_layout(),
            #section "Weather Data"
            weather_data_layout(),
            # fourth container, for the soil moisture data
            # soil_moisture_layout(),
            # fifth container, for the description of the lorawan technology
            hintergrund_section(),
            # sixth container, for the description of the lorawan technology
            footer(),
        ]

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)
