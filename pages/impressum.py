import dash_bootstrap_components as dbc
from dash import html, dcc

def impressum_layout():
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col(
                    html.Div(dcc.Markdown("""
**IMPRESSUM**

**Angaben gemäß § 5 TMG:**

Land l(i)eben – digital.gemeinsam.vorOrt

Kreisverwaltung Kusel

Trierer Str. 49-51

66869 Kusel



**Vertreten durch:**

Kreisverwaltung Kusel

vertreten durch den Landrat Otto Rubly



**Kontakt:**

Otto Rubly

Trierer Straße 49-51

66869 Kusel

Telefon: 06381/ 424-0

E-Mail: landlieben@kv-kus.de



**Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV:**

Kreisverwaltung Kusel

Landrat Otto Rubly

Trierer Straße 49-51

66869 Kusel

Telefon: +49 6381 424 0

Telefax: +49 6381 424 440

E-Mail: buergerbuero@kv-kus.de

Internet: https://www.landkreis-kusel.de

Der Landkreis Kusel ist eine Körperschaft des Öffentlichen Rechts. Der Landkreis wird vertreten durch Herrn Landrat Otto Rubly.



**Webhostinganbietende**

PythonAnywhere LLP

5 The Green,

Richmond TW9 1PL

United Kingdom



**Streitschlichtung**

Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit:

https://ec.europa.eu/consumers/odr

Unsere E-Mail-Adresse finden Sie oben im Impressum.

Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.



**Haftung für Inhalte**

Als Diensteanbietende sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nichtverpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.

Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.


**Urheberrecht**

Die durch die Seitenbetreibende erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers. Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet.

Soweit die Inhalte auf dieser Seite nicht vom Betreibenden erstellt wurden, werden die Urheberrechte Dritter beachtet. Insbesondere werden Inhalte Dritter als solche gekennzeichnet. Sollten Sie trotzdem auf eine Urheberrechtsverletzung aufmerksam werden, bitten wir um einen entsprechenden Hinweis. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Inhalte umgehend entfernen.



**Credits**

Bildnachweise

Alle auf dieser Seite verwendeten Bilder, Fotos, Logos, Texte dürfen nur nach Rücksprache mit der Redaktion weiterverwendet werden. 

Die verwendeten Bilder auf dieser Seite stammen von folgenden Quellen: 

icon-icons.com/de

Pixabay.com

Eigene Fotografien/Quellen oder durch Dritte, von uns Beauftragten. 

In jedem Fall wird die Bildquelle angegeben.


**Quelle** 

https://www.e-recht24.de/impressum-generator.html


                    """, className="text-black m-5", style={"lineHeight": "250%", })),
                    lg=12, md=12, sm=12, width=12, xl=12, xs=12
                ),
            ])
        ])
    ])
