import dash
from dash import html
import dash_bootstrap_components as dbc
from components.jumbotron import jumbotron
from components.weather_station_section import create_temperature_graph, create_precipitation_graph, weather_text_content, weather_now_text_content, weather_data_layout
from components.project_description_section import project_description_section
from components.soil_moisture_section import soil_moisture_layout
from components.tree_monitoring import tree_layout
from components.navbar import Navbar

jumbotron = jumbotron()

app = dash.Dash(__name__, meta_tags=[
        {'name': 'viewport', 'content': 'width=device-width, initial-scale=1, maximum-scale=1.2, minimum-scale=0.5'}],
        external_stylesheets=[dbc.themes.SANDSTONE, "/assets/style.css"], )

app.title = "Sensornetz Smart City"

app.layout = dbc.Container(children=[
    Navbar(),
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
    #fifth container, for the tree monitoring
    tree_layout(),
],

fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
