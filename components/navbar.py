import dash_bootstrap_components as dbc
from config import NAVBAR_URLS
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

logo = r"\assets\logo_landlieben.png"

def Navbar():
    return dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=logo, height="40px")),
                            dbc.Col(dbc.NavbarBrand("Sensornetz LAND L(i)EBEN", className="ms-2 d-none d-lg-block")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href='http://127.0.0.1:8050',
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                    children=[
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Home", href=NAVBAR_URLS['home'], className='text-end')),
                                dbc.NavItem(dbc.NavLink("Über das Projekt", href=NAVBAR_URLS['project'], className='text-end')),
                                dbc.NavItem(dbc.NavLink("Baummonitoring", href=NAVBAR_URLS['soil_moisture'], className='text-end')),
                                dbc.NavItem(dbc.NavLink("Wetterdaten", href=NAVBAR_URLS['weather'], className='text-end')),
                                dbc.NavItem(dbc.NavLink("Weitere Infos", href=NAVBAR_URLS['weitere_infos'], className='text-end')),

                            ],
                            className="ms-auto",
                        )
                    ],
                ),
            ]
        ),
        color="dark",
        dark=True,
    )




# def Navbar():
#     return dbc.NavbarSimple(
#         children=[
#             dbc.NavItem(dbc.NavLink("Home", href=NAVBAR_URLS['home'])),
#             dbc.NavItem(dbc.NavLink("Über das Projekt", href=NAVBAR_URLS['project'])),
#             dbc.NavItem(dbc.NavLink("Baummonitoring", href=NAVBAR_URLS['soil_moisture'])),
#             dbc.NavItem(dbc.NavLink("Wetterdaten", href=NAVBAR_URLS['weather'])),
#             dbc.NavItem(dbc.NavLink("Weitere Infos", href=NAVBAR_URLS['weitere_infos'])),
#         ],
#         brand="Sensornetz LAND L(i)EBEN",
#         brand_href="https://www.landschaft-lieben.de",
#         color="black",
#         dark=True,
#         className="sticky-navbar sticky-top"
#     )


