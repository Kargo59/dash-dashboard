import dash
from dash import html
import dash_bootstrap_components as dbc
from components.jumbotron import jumbotron
from components.weather_station_section import create_temperature_graph, create_precipitation_graph, weather_text_content, weather_now_text_content, weather_data_layout
from components.project_description_section import project_description_section
from components.soil_moisture_section import soil_moisture_layout
from config import NAVBAR_URLS


jumbotron = jumbotron()

app = dash.Dash(__name__, meta_tags=[
        {'name': 'viewport', 'content': 'width=device-width, initial-scale=1, maximum-scale=1.2, minimum-scale=0.5'}],
        external_stylesheets=[dbc.themes.SANDSTONE, "/assets/style.css"], )

app.title = "Sensornetz Smart City"

app.layout = dbc.Container(children=[
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href=NAVBAR_URLS['home'])),
            dbc.NavItem(dbc.NavLink("Über das Projekt", href=NAVBAR_URLS['project'])),
            dbc.NavItem(dbc.NavLink("Wetterdaten", href=NAVBAR_URLS['weather'])),
            dbc.NavItem(dbc.NavLink("Bodenfeuchte", href=NAVBAR_URLS['soil_moisture'])),
        ],
        brand="Sensornetz Land Lieben",
        brand_href="#",
        color="primary",
        dark=True,
    className="sticky-top"),
    # first container for the tile and the background thats going to be paralaxxed
    html.Div([
        html.Div(jumbotron, className="position-absolute bottom-0 end-0"),
    ], className="parallax-container", id='top'),
    #section "About the project"
    project_description_section(),
    #section "Weather Data"
    weather_data_layout(),
    # fourth container, for the soil moisture data
    soil_moisture_layout(),
],

fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
