import dash_bootstrap_components as dbc
from dash import html, dcc


def hintergrund_section():
    return html.Div([
        # Project Description
        dbc.Row([
            dbc.Col(html.H1("Weiterführende Informationen", id="hintergrund", className="text-center mt-5 mb-5"), width=12)
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    # Description
                                    dbc.Row([
                                        dbc.Col(
                                            html.Div(dcc.Markdown("""
                                                            Das Sensoren-Netzwerk im Landkreis Kusel besteht aus mehreren Komponenten: 
                                                            den Messgeräten, in diesem Fall Sensoren (z.B. Bodenfeuchtesensor und Wetterstation) 
                                                            und dem sogenannten Gateway (Netzwerkknoten). 
                                                            Sensoren messen Umweltbedingungen, wie zum Beispiel Temperatur, Feuchtigkeit oder 
                                                            auch Bewegung und senden die Informationen bzw. Daten an das Gateway. Das Gateway 
                                                            empfängt die Messdaten über die sogenannte LoRaWan-Funktechnologie. LoRaWAN (Long
                                                            Range Wide Area Network) bezeichnet ein drahtloses System zum verschlüsselten 
                                                            Datenaustausch über weite Strecken. Die Messdaten der Sensoren werden in 
                                                            regelmäßigen Abständen über Radiowellen ausgesendet und empfangen. 
                                                            Das Gateway sendet die empfangenen Messdaten an einen Datenspeicher, 
                                                            sogenannte Server. Alle Messdaten, die auf dem Server zusammenfließen 
                                                            werden auf dieser Webseite veranschaulicht und stehen somit öffentlich 
                                                            für alle zur Verfügung.  
                                                            Die Experimentierfläche an der Burg Lichtenberg gibt den Startschuss zum Aufbau 
                                                            eines landkreisweiten Sensorik-Netzwerks. 

                                            """, className="text-black m-5", style={"lineHeight": "250%", })),
                                            lg=12, md=12, sm=12, width=12, xl=12, xs=12
                                        ),

                                    ], className="", justify="center"),
                                ],
                                title="Technischer Hintergrund",
                            ),
                            # Add other accordion items as necessary
                            dbc.AccordionItem(
                                [
                                    # Description
                                    dbc.Row([
                                        dbc.Col(
                                            html.Div(dcc.Markdown("""
                                            Im Rahmen der „Klimafitchallenge“ der Kreisverwaltung Kusel im Jahr 2021 
                                            wurde mit Unterstützung der Kreissparkasse Kusel in direkter Nähe zur Burg
                                            Lichtenberg eine Streuobstwiese mit 15 Bäumen angepflanzt. Durch 
                                            umweltbewusstes Verhalten konnten die Mitarbeitenden jede Menge Punkte 
                                            sammeln und so 1,2 Tonnen CO2 einsparen. Am Ende der Aktion wurden die 
                                            Punkte aller Mitarbeitenden gegen 15 Obstbäume eingetauscht, die im 
                                            Frühjahr 2022 eingepflanzt wurden. Die Schüler und Schülerinnen der 
                                            BBS Kusel schenkten der Fläche in Zusammenarbeit mit dem TRAFO-Projekt 
                                            des Landkreises zudem zwei selbstgebaute Insektenhotels in Form von 
                                            Musikinstrumenten – passend zum Kuseler Wandermusikantenland. Seit 
                                            September 2023 ist die Fläche neben den längeren (Premium-)Wanderwegen 
                                            auch Teil eines eigens dafür angelegten und 3,2 Kilometer langen 
                                            Streuobstwiesenwanderweges. 

                                            """, className="text-black m-5", style={"lineHeight": "250%", })),
                                            lg=12, md=12, sm=12, width=12, xl=12, xs=12
                                        ),
                                    ], className="", justify="center"),
                                ],
                                title="Mehr zur Streuobstwiese",
                            ),
                            dbc.AccordionItem(
                                [
                                    # Description
                                    dbc.Row([
                                        dbc.Col(
                                            html.Div(dcc.Markdown("""
                                            Im Rahmen des Förderprojektes „Smart Cities“ des Bundesministeriums
                                            für Wohnen, Stadtentwicklung und Bauwesen in Kooperation mit der KfW 
                                            wurde der Landkreis Kusel unter dem Motto „LAND L(i)EBEN – 
                                            digital.gemeinsam.vorOrt“ als Modellprojekt ausgewählt. Ein Auftrag von 
                                            LAND L(i)EBEN ist der Aufbau von grundlegenden technischen Infrastrukturen 
                                            im Landkreis Kusel. Diese Technik wird eingesetzt um das ländliche Naturgut 
                                            langfristig zu schützen und somit für die schöne Landschaft Sorge zu 
                                            tragen. Gleichzeitig kommen die Erprobung und die gewonnenen Erfahrungen 
                                            im Umgang mit der Technik später einmal der Landwirtschaft, 
                                            Landschaftsvereinen und dem Gartenbau zugute.  

                                            """, className="text-black m-5", style={"lineHeight": "250%", })),
                                            lg=12, md=12, sm=12, width=12, xl=12, xs=12
                                        ),
                                    ], className="", justify="center"),
                                ],
                                title="Mehr zu LAND L(I)EBEN",
                            ),
                        ],
                        start_collapsed=True)
                ),
                lg=8, md=12, sm=12, width=4, xl=8, xs=12
            ),
        ], className="rounded", justify="center"),
    ]
    )
