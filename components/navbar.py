import dash_bootstrap_components as dbc
from config import NAVBAR_URLS

def Navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href=NAVBAR_URLS['home'])),
            dbc.NavItem(dbc.NavLink("Über das Projekt", href=NAVBAR_URLS['project'])),
            dbc.NavItem(dbc.NavLink("Wetterdaten", href=NAVBAR_URLS['weather'])),
            dbc.NavItem(dbc.NavLink("Bodenfeuchte", href=NAVBAR_URLS['soil_moisture'])),
        ],
        brand="Sensornetz Land Lieben",
        brand_href="#",
        color="black",
        dark=True,
        className="sticky-top"
    )