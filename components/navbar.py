import dash_bootstrap_components as dbc
from config import NAVBAR_URLS

def Navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Home", href=NAVBAR_URLS['home'])),
            dbc.NavItem(dbc.NavLink("Über das Projekt", href=NAVBAR_URLS['project'])),
            dbc.NavItem(dbc.NavLink("Baummonitoring", href=NAVBAR_URLS['soil_moisture'])),
            dbc.NavItem(dbc.NavLink("Wetterdaten", href=NAVBAR_URLS['weather'])),
            dbc.NavItem(dbc.NavLink("Weitere Infos", href=NAVBAR_URLS['weitere_infos'])),
        ],
        brand="Sensornetz Land Lieben",
        brand_href="",
        color="black",
        dark=True,
        className="sticky-navbar sticky-top"
    )
