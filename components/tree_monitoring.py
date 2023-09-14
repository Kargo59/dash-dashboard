import dash_bootstrap_components as dbc
from dash import html, dcc

def tree_layout():
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.H1("Welche Bäume müssen bewässert werden?", className="text-center"), width=12),  # New column with H1 title
                    dbc.Col(  # New Column to contain the inner Row
                        dbc.Row(
                            [
                                dbc.Col(html.Div([
                                    html.Img(src='/assets/tree.svg', className='img-fluid rounded-circle mx-auto d-block m-5 icon-responsive',
                                             alt="Responsive image", style={'background-color': "#86eb34"}),
                                    dcc.Markdown('''
                                        **Baum 1**
                                    ''', className="text-center")
                                ]), width=4),
                                dbc.Col(html.Div([
                                    html.Img(src='/assets/tree.svg', className='img-fluid rounded-circle mx-auto d-block m-5 icon-responsive',
                                             alt="Responsive image", style={'background-color': "#f4fc03"}),
                                    dcc.Markdown('''
                                        **Baum 2**
                                    ''', className="text-center")
                                ]), width=4),
                                dbc.Col(html.Div([
                                    html.Img(src='/assets/tree.svg', className='img-fluid rounded-circle mx-auto d-block m-5 icon-responsive',
                                             alt="Responsive image", style={'background-color': "#fc0303"}),
                                    dcc.Markdown('''
                                        **Baum 3**
                                    ''', className="text-center")
                                ]), width=4),
                            ],
                            justify='center', className='m-5'
                        )
                    )
                ]
            )
        ],
        className="my-section-wrapper"  # This is just an example. You can add any class or style you want here.
    )

