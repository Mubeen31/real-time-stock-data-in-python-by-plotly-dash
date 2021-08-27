import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
from datetime import datetime

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src = app.get_asset_url('financial-profit.png'),
                     style = {'height': '30px'},
                     ),
            html.H6('Real time Crypto currency data',
                    style = {'color': 'black'},
                    className = 'title'
                    ),
        ], className = 'logo_title'),
        html.Div([
            html.H6(id = 'get_date_time',
                    style = {'color': 'black'},
                    )
        ], className = 'adjust_date_time twelve columns')
    ], className = "row flex-display"),
    html.Div([
        dcc.Interval(id = 'update_date_time',
                     interval = 1000,
                     n_intervals = 0),
    ]),

    html.Div([
        dcc.Interval(id = 'update_value',
                     interval = 5000,
                     n_intervals = 0),
    ]),

    html.Div([
        html.Div([
            html.Div([
                html.Div(id = 'text_row1'),
                html.Div(id = 'text_row2', className = 'text_row2'),

            ], className = 'create_container three columns'),
            html.Div([
                html.Div(id = 'text_row3'),
                html.Div(id = 'text_row4', className = 'text_row2'),

            ], className = 'create_container three columns'),

            html.Div([
                html.Div(id = 'text_row5'),
                html.Div(id = 'text_row6', className = 'text_row2'),

            ], className = 'create_container three columns'),

            html.Div([
                html.Div(id = 'text_row7'),
                html.Div(id = 'text_row8', className = 'text_row2'),

            ], className = 'create_container three columns'),
        ], className = 'container_gap twelve columns')

    ], className = "row flex-display"),

    html.Div([
        html.Div([
            html.Div(id = 'table_data', className = 'table_width'),
            dcc.Graph(id = 'bitcoin_chart',
                      animate = True,
                      config = {'displayModeBar': 'hover'},
                      className = 'chart_width'),
        ], className = 'second_row twelve columns')
    ], className = "row flex-display")

], id= "mainContainer",
   style={"display": "flex", "flex-direction": "column"})

@app.callback(Output('get_date_time', 'children'),
              [Input('update_date_time', 'n_intervals')])
def update_graph(n_intervals):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    if n_intervals == 0:
        raise PreventUpdate

    return [
        html.Div(dt_string),
    ]


@app.callback(Output('text_row1', 'children'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'CryptoCurrency', 'Price', 'price_difference', 'Change (24h) %', 'Market Cap.']
    bitcoin_df = pd.read_csv('bitcoin_data.csv', names = header_list)
    bitcoin_df['price_difference'] = bitcoin_df['Price'].diff()
    price_difference = bitcoin_df['price_difference'].tail(1).iloc[0]
    bitcoin_price = bitcoin_df['Price'].tail(1).iloc[0]
    if n_intervals == 0:
        raise PreventUpdate

    if price_difference > 0:
        return [
            html.P('Bitcoin',
                   style = {'textAlign': 'left',
                            'color': 'Black',
                            'fontSize': 17,
                            }
                   ),
            html.Div([
                html.Div([
                    html.H6('{0:,.2f}'.format(bitcoin_price),
                            style = {'textAlign': 'left',
                                     'color': '#00cc00',
                                     'margin-top': '-8px',
                                     'font-weight': 'bold'
                                     }
                            ),
                    html.I(className = "fas fa-arrow-up",
                           style = {"font-size": "120%",
                                    'margin-top': '-1px',
                                    'color': '#00cc00'}),

                ], className = 'adjust_image'),
                html.P('${0:,.0f}'.format(bitcoin_price),
                       style = {'textAlign': 'left',
                                'color': '#808080',
                                'fontSize': 14,
                                'margin-top': '-2px',
                                }, className = 'margin_left_value'
                       ),
            ], className = 'adjust_price')

        ]
    elif price_difference < 0:
        return [
            html.P('Bitcoin',
                   style = {'textAlign': 'left',
                            'color': 'Black',
                            'fontSize': 17,
                            }
                   ),
            html.Div([
                html.Div([
                    html.H6('{0:,.2f}'.format(bitcoin_price),
                            style = {'textAlign': 'left',
                                     'color': '#EC1E3D',
                                     'margin-top': '-8px',
                                     'font-weight': 'bold'
                                     }
                            ),
                    html.I(className = "fas fa-arrow-down",
                           style = {"font-size": "120%",
                                    'margin-top': '-1px',
                                    'color': '#EC1E3D'}),

                ], className = 'adjust_image'),
                html.P('${0:,.0f}'.format(bitcoin_price),
                       style = {'textAlign': 'left',
                                'color': '#808080',
                                'fontSize': 14,
                                'margin-top': '-2px',
                                }, className = 'margin_left_value'
                       ),
            ], className = 'adjust_price')

        ]
    elif price_difference == 0:
        return [
            html.P('Bitcoin',
                   style = {'textAlign': 'left',
                            'color': 'Black',
                            'fontSize': 17,
                            }
                   ),
            html.Div([
                html.Div([
                    html.H6('{0:,.2f}'.format(bitcoin_price),
                            style = {'textAlign': 'left',
                                     'color': 'black',
                                     'margin-top': '-8px',
                                     'font-weight': 'bold'
                                     }
                            ),

                ], className = 'adjust_image'),
                html.P('${0:,.0f}'.format(bitcoin_price),
                       style = {'textAlign': 'left',
                                'color': '#808080',
                                'fontSize': 14,
                                'margin-top': '-2px',
                                }, className = 'margin_left_value'
                       ),
            ], className = 'adjust_price')

        ]

@app.callback(Output('text_row2', 'children'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']
    bitcoin_df = pd.read_csv('bitcoin_data.csv', names = header_list)
    change_24h = bitcoin_df['Change (24h) %'].tail(1).iloc[0]
    market_cap = bitcoin_df['Market Cap.'].tail(1).iloc[0]
    if n_intervals == 0:
        raise PreventUpdate

    if change_24h > 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': '#00cc00',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-up",
                               style = {"font-size": "80%",
                                        'margin-top': '-5px',
                                        'color': '#00cc00'}),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]
    elif change_24h < 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': '#EC1E3D',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-down",
                               style = {"font-size": "80%",
                                        'margin-top': '-5px',
                                        'color': '#EC1E3D'}),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]
    elif change_24h == 0:
        return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]

@app.callback(Output('text_row3', 'children'),
                [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'CryptoCurrency', 'Price', 'price_difference', 'Change (24h) %', 'Market Cap.']
    ethereum_df = pd.read_csv('ethereum_data.csv', names = header_list)
    ethereum_df['price_difference'] = ethereum_df['Price'].diff()
    price_difference = ethereum_df['price_difference'].tail(1).iloc[0]
    ethereum_price = ethereum_df['Price'].tail(1).iloc[0]
    if n_intervals == 0:
        raise PreventUpdate

    if price_difference > 0:
            return [
                html.P('Ethereum',
                       style = {'textAlign': 'left',
                                'color': 'Black',
                                'fontSize': 17,
                                }
                       ),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(ethereum_price),
                                style = {'textAlign': 'left',
                                         'color': '#00cc00',
                                         'margin-top': '-8px',
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-up",
                               style = {"font-size": "120%",
                                        'margin-top': '-1px',
                                        'color': '#00cc00'}),

                    ], className = 'adjust_image'),
                    html.P('${0:,.0f}'.format(ethereum_price),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 14,
                                    'margin-top': '-2px',
                                    }, className = 'margin_left_value'
                           ),
                ], className = 'adjust_price')

            ]
    elif price_difference < 0:
            return [
                html.P('Ethereum',
                       style = {'textAlign': 'left',
                                'color': 'Black',
                                'fontSize': 17,
                                }
                       ),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(ethereum_price),
                                style = {'textAlign': 'left',
                                         'color': '#EC1E3D',
                                         'margin-top': '-8px',
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-down",
                               style = {"font-size": "120%",
                                        'margin-top': '-1px',
                                        'color': '#EC1E3D'}),

                    ], className = 'adjust_image'),
                    html.P('${0:,.0f}'.format(ethereum_price),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 14,
                                    'margin-top': '-2px',
                                    }, className = 'margin_left_value'
                           ),
                ], className = 'adjust_price')

            ]
    elif price_difference == 0:
            return [
                html.P('Ethereum',
                       style = {'textAlign': 'left',
                                'color': 'Black',
                                'fontSize': 17,
                                }
                       ),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(ethereum_price),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '-8px',
                                         'font-weight': 'bold'
                                         }
                                ),

                    ], className = 'adjust_image'),
                    html.P('${0:,.0f}'.format(ethereum_price),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 14,
                                    'margin-top': '-2px',
                                    }, className = 'margin_left_value'
                           ),
                ], className = 'adjust_price')

            ]

@app.callback(Output('text_row4', 'children'),
                [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']
    ethereum_df = pd.read_csv('ethereum_data.csv', names = header_list)
    change_24h = ethereum_df['Change (24h) %'].tail(1).iloc[0]
    market_cap = ethereum_df['Market Cap.'].tail(1).iloc[0]
    if n_intervals == 0:
        raise PreventUpdate

    if change_24h > 0:
            return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': '#00cc00',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-up",
                               style = {"font-size": "80%",
                                        'margin-top': '-5px',
                                        'color': '#00cc00'}),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]
    elif change_24h < 0:
            return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': '#EC1E3D',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-down",
                               style = {"font-size": "80%",
                                        'margin-top': '-5px',
                                        'color': '#EC1E3D'}),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]
    if change_24h == 0:
            return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]
@app.callback(Output('text_row5', 'children'),
                [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'CryptoCurrency', 'Price', 'price_difference', 'Change (24h) %', 'Market Cap.']
    binance_df = pd.read_csv('binance_data.csv', names = header_list)
    binance_df['price_difference'] = binance_df['Price'].diff()
    price_difference = binance_df['price_difference'].tail(1).iloc[0]
    binance_price = binance_df['Price'].tail(1).iloc[0]
    if n_intervals == 0:
        raise PreventUpdate

    if price_difference > 0:
            return [
                html.P('Binance Coin',
                       style = {'textAlign': 'left',
                                'color': 'Black',
                                'fontSize': 17,
                                }
                       ),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(binance_price),
                                style = {'textAlign': 'left',
                                         'color': '#00cc00',
                                         'margin-top': '-8px',
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-up",
                               style = {"font-size": "120%",
                                        'margin-top': '-1px',
                                        'color': '#00cc00'}),

                    ], className = 'adjust_image'),
                    html.P('${0:,.0f}'.format(binance_price),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 14,
                                    'margin-top': '-2px',
                                    }, className = 'margin_left_value'
                           ),
                ], className = 'adjust_price')

            ]
    elif price_difference < 0:
            return [
                html.P('Binance Coin',
                       style = {'textAlign': 'left',
                                'color': 'Black',
                                'fontSize': 17,
                                }
                       ),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(binance_price),
                                style = {'textAlign': 'left',
                                         'color': '#EC1E3D',
                                         'margin-top': '-8px',
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-down",
                               style = {"font-size": "120%",
                                        'margin-top': '-1px',
                                        'color': '#EC1E3D'}),

                    ], className = 'adjust_image'),
                    html.P('${0:,.0f}'.format(binance_price),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 14,
                                    'margin-top': '-2px',
                                    }, className = 'margin_left_value'
                           ),
                ], className = 'adjust_price')

            ]
    elif price_difference == 0:
            return [
                html.P('Binance Coin',
                       style = {'textAlign': 'left',
                                'color': 'Black',
                                'fontSize': 17,
                                }
                       ),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(binance_price),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '-8px',
                                         'font-weight': 'bold'
                                         }
                                ),

                    ], className = 'adjust_image'),
                    html.P('${0:,.0f}'.format(binance_price),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 14,
                                    'margin-top': '-2px',
                                    }, className = 'margin_left_value'
                           ),
                ], className = 'adjust_price')

            ]

@app.callback(Output('text_row6', 'children'),
                [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']
    binance_df = pd.read_csv('binance_data.csv', names = header_list)
    change_24h = binance_df['Change (24h) %'].tail(1).iloc[0]
    market_cap = binance_df['Market Cap.'].tail(1).iloc[0]
    if n_intervals == 0:
        raise PreventUpdate

    if change_24h > 0:
            return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': '#00cc00',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-up",
                               style = {"font-size": "80%",
                                        'margin-top': '-5px',
                                        'color': '#00cc00'}),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]
    elif change_24h < 0:
            return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': '#EC1E3D',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-down",
                               style = {"font-size": "80%",
                                        'margin-top': '-5px',
                                        'color': '#EC1E3D'}),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]
    if change_24h == 0:
            return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]
@app.callback(Output('text_row7', 'children'),
                [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'CryptoCurrency', 'Price', 'price_difference', 'Change (24h) %', 'Market Cap.']
    bitcoincash_df = pd.read_csv('bitcoincash_data.csv', names = header_list)
    bitcoincash_df['price_difference'] = bitcoincash_df['Price'].diff()
    price_difference = bitcoincash_df['price_difference'].tail(1).iloc[0]
    bitcoincash_price = bitcoincash_df['Price'].tail(1).iloc[0]
    if n_intervals == 0:
        raise PreventUpdate

    if price_difference > 0:
            return [
                html.P('Bitcoin Cash',
                       style = {'textAlign': 'left',
                                'color': 'Black',
                                'fontSize': 17,
                                }
                       ),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(bitcoincash_price),
                                style = {'textAlign': 'left',
                                         'color': '#00cc00',
                                         'margin-top': '-8px',
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-up",
                               style = {"font-size": "120%",
                                        'margin-top': '-1px',
                                        'color': '#00cc00'}),

                    ], className = 'adjust_image'),
                    html.P('${0:,.0f}'.format(bitcoincash_price),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 14,
                                    'margin-top': '-2px',
                                    }, className = 'margin_left_value'
                           ),
                ], className = 'adjust_price')

            ]
    elif price_difference < 0:
            return [
                html.P('Bitcoin Cash',
                       style = {'textAlign': 'left',
                                'color': 'Black',
                                'fontSize': 17,
                                }
                       ),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(bitcoincash_price),
                                style = {'textAlign': 'left',
                                         'color': '#EC1E3D',
                                         'margin-top': '-8px',
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-down",
                               style = {"font-size": "120%",
                                        'margin-top': '-1px',
                                        'color': '#EC1E3D'}),

                    ], className = 'adjust_image'),
                    html.P('${0:,.0f}'.format(bitcoincash_price),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 14,
                                    'margin-top': '-2px',
                                    }, className = 'margin_left_value'
                           ),
                ], className = 'adjust_price')

            ]
    elif price_difference == 0:
            return [
                html.P('Bitcoin Cash',
                       style = {'textAlign': 'left',
                                'color': 'Black',
                                'fontSize': 17,
                                }
                       ),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(bitcoincash_price),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '-8px',
                                         'font-weight': 'bold'
                                         }
                                ),

                    ], className = 'adjust_image'),
                    html.P('${0:,.0f}'.format(bitcoincash_price),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 14,
                                    'margin-top': '-2px',
                                    }, className = 'margin_left_value'
                           ),
                ], className = 'adjust_price')

            ]

@app.callback(Output('text_row8', 'children'),
                [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']
    bitcoincash_df = pd.read_csv('bitcoincash_data.csv', names = header_list)
    change_24h = bitcoincash_df['Change (24h) %'].tail(1).iloc[0]
    market_cap = bitcoincash_df['Market Cap.'].tail(1).iloc[0]
    if n_intervals == 0:
        raise PreventUpdate

    if change_24h > 0:
            return [
                html.Div([
                    html.Div([
                        html.H6('+{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': '#00cc00',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-up",
                               style = {"font-size": "80%",
                                        'margin-top': '-5px',
                                        'color': '#00cc00'}),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]
    elif change_24h < 0:
            return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': '#EC1E3D',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),
                        html.I(className = "fas fa-arrow-down",
                               style = {"font-size": "80%",
                                        'margin-top': '-5px',
                                        'color': '#EC1E3D'}),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]
    if change_24h == 0:
            return [
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}%'.format(change_24h),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '-8px',
                                         'fontSize': 12,
                                         'font-weight': 'bold'
                                         }
                                ),

                    ], className = 'adjust_image_row2'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]

@app.callback(Output('table_data', 'children'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']
    chainlink_df = pd.read_csv('chainlink_data.csv', names = header_list)
    chainlink_price = chainlink_df['Price'].tail(1).iloc[0]
    chainlink_change_24h = chainlink_df['Change (24h) %'].tail(1).iloc[0]
    chainlink_market_cap = chainlink_df['Market Cap.'].tail(1).iloc[0]

    header_list = ['Time', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']
    bitcoin_df = pd.read_csv('bitcoin_data.csv', names = header_list)
    bitcoin_price = bitcoin_df['Price'].tail(1).iloc[0]
    bitcoin_change_24h = bitcoin_df['Change (24h) %'].tail(1).iloc[0]
    bitcoin_market_cap = bitcoin_df['Market Cap.'].tail(1).iloc[0]

    header_list = ['Time', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']
    ethereum_df = pd.read_csv('ethereum_data.csv', names = header_list)
    ethereum_price = ethereum_df['Price'].tail(1).iloc[0]
    ethereum_change_24h = ethereum_df['Change (24h) %'].tail(1).iloc[0]
    ethereum_market_cap = ethereum_df['Market Cap.'].tail(1).iloc[0]

    header_list = ['Time', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']
    binancecoin_df = pd.read_csv('binance_data.csv', names = header_list)
    binancecoin_price = binancecoin_df['Price'].tail(1).iloc[0]
    binancecoin_change_24h = binancecoin_df['Change (24h) %'].tail(1).iloc[0]
    binancecoin_market_cap = binancecoin_df['Market Cap.'].tail(1).iloc[0]

    header_list = ['Time', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']
    bitcoincash_df = pd.read_csv('bitcoincash_data.csv', names = header_list)
    bitcoincash_price = bitcoincash_df['Price'].tail(1).iloc[0]
    bitcoincash_change_24h = bitcoincash_df['Change (24h) %'].tail(1).iloc[0]
    bitcoincash_market_cap = bitcoincash_df['Market Cap.'].tail(1).iloc[0]

    if n_intervals == 0:
        raise PreventUpdate

    return [

        html.Table([
            html.Thead(
                html.Tr([
                    html.Th('#', style = {'width': '30px'}),
                    html.Th('Crypto Currency', style = {'width': '120px'},
                                               className = 'crypto_column'),
                    html.Th('Price', style = {'width': '120px'}),
                    html.Th('Change (24)', style = {'width': '90px'}),
                    html.Th('Market Cap.', style = {'width': '150px'})
                ], className = 'header_hover')
            ),
            html.Tbody([
                html.Tr([
                    html.Td(html.P('1', style = {'textAlign': 'left',
                                                 'color': 'black',
                                                 'fontSize': 12,
                                                 'margin-top': '10px',
                                                 }),
                            ),
                    html.Td(html.Div([
                        html.Img(src = app.get_asset_url('chainlink.png'),
                                 style = {'height': '30px'},
                                 className = 'image'),
                        html.P('Chainlink', style = {'margin-left': '-12px'},
                                            className = 'logo_text'
                               )
                    ], className = 'logo_image'),
                    ),
                    html.Td(
                        html.H6('${0:,.2f}'.format(chainlink_price),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '10px',
                                         'fontSize': 12,
                                         }
                                ),

                    ),
                    html.Td(
                            html.H6('{0:,.2f}%'.format(chainlink_change_24h),
                                    style = {'textAlign': 'left',
                                             'color': 'black',
                                             'margin-top': '10px',
                                             'fontSize': 12,
                                             }
                                    ),
                    ),
                    html.Td(
                        html.P('${0:,.0f}'.format(chainlink_market_cap),
                               style = {'textAlign': 'left',
                                        'color': 'black',
                                        'fontSize': 12,
                                        'margin-top': '10px',
                                        }),
                    ),
                ], className = 'hover_only_row'),

                html.Tr([
                    html.Td(html.P('2', style = {'textAlign': 'left',
                                                 'color': 'black',
                                                 'fontSize': 12,
                                                 'margin-top': '10px',
                                                 }),
                            ),
                    html.Td(html.Div([
                        html.Img(src = app.get_asset_url('bitcoin.png'),
                                 style = {'height': '30px'},
                                 className = 'image'),
                        html.P('Bitcoin', style = {'margin-left': '-3px'},
                                          className = 'logo_text')
                    ], className = 'logo_image'),
                    ),
                    html.Td(
                        html.H6('${0:,.2f}'.format(bitcoin_price),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '10px',
                                         'fontSize': 12,
                                         }
                                ),

                    ),
                    html.Td(
                        html.H6('{0:,.2f}%'.format(bitcoin_change_24h),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '10px',
                                         'fontSize': 12,
                                         }
                                ),
                    ),
                    html.Td(
                        html.P('${0:,.0f}'.format(bitcoin_market_cap),
                               style = {'textAlign': 'left',
                                        'color': 'black',
                                        'fontSize': 12,
                                        'margin-top': '10px',
                                        }),
                    ),
                ], className = 'hover_only_row'),

                html.Tr([
                    html.Td(html.P('3', style = {'textAlign': 'left',
                                                 'color': 'black',
                                                 'fontSize': 12,
                                                 'margin-top': '10px',
                                                 }),
                            ),
                    html.Td(html.Div([
                        html.Img(src = app.get_asset_url('ethereum.png'),
                                 style = {'height': '30px'},
                                 className = 'image'),
                        html.P('Ethereum', style = {'margin-left': '-15px'},
                               className = 'logo_text')
                    ], className = 'logo_image'),
                    ),
                    html.Td(
                        html.H6('${0:,.2f}'.format(ethereum_price),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '10px',
                                         'fontSize': 12,
                                         }
                                ),

                    ),
                    html.Td(
                        html.H6('{0:,.2f}%'.format(ethereum_change_24h),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '10px',
                                         'fontSize': 12,
                                         }
                                ),
                    ),
                    html.Td(
                        html.P('${0:,.0f}'.format(ethereum_market_cap),
                               style = {'textAlign': 'left',
                                        'color': 'black',
                                        'fontSize': 12,
                                        'margin-top': '10px',
                                        }),
                    ),
                ], className = 'hover_only_row'),

                html.Tr([
                    html.Td(html.P('4', style = {'textAlign': 'left',
                                                 'color': 'black',
                                                 'fontSize': 12,
                                                 'margin-top': '10px',
                                                 }),
                            ),
                    html.Td(html.Div([
                        html.Img(src = app.get_asset_url('binance.png'),
                                 style = {'height': '30px'},
                                 className = 'image'),
                        html.P('Binance Coin', style = {'margin-left': '-25px'},
                               className = 'logo_text')
                    ], className = 'logo_image'),
                    ),
                    html.Td(
                        html.H6('${0:,.2f}'.format(binancecoin_price),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '10px',
                                         'fontSize': 12,
                                         }
                                ),

                    ),
                    html.Td(
                        html.H6('{0:,.2f}%'.format(binancecoin_change_24h),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '10px',
                                         'fontSize': 12,
                                         }
                                ),
                    ),
                    html.Td(
                        html.P('${0:,.0f}'.format(binancecoin_market_cap),
                               style = {'textAlign': 'left',
                                        'color': 'black',
                                        'fontSize': 12,
                                        'margin-top': '10px',
                                        }),
                    ),
                ], className = 'hover_only_row'),

                html.Tr([
                    html.Td(html.P('5', style = {'textAlign': 'left',
                                                 'color': 'black',
                                                 'fontSize': 12,
                                                 'margin-top': '10px',
                                                 }),
                            ),
                    html.Td(html.Div([
                        html.Img(src = app.get_asset_url('bitcoincash.png'),
                                 style = {'height': '30px'},
                                 className = 'image'),
                        html.P('Bitcoin Cash', style = {'margin-left': '-23px'},
                               className = 'logo_text')
                    ], className = 'logo_image'),
                    ),
                    html.Td(
                        html.H6('${0:,.2f}'.format(bitcoincash_price),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '10px',
                                         'fontSize': 12,
                                         }
                                ),

                    ),
                    html.Td(
                        html.H6('{0:,.2f}%'.format(bitcoincash_change_24h),
                                style = {'textAlign': 'left',
                                         'color': 'black',
                                         'margin-top': '10px',
                                         'fontSize': 12,
                                         }
                                ),
                    ),
                    html.Td(
                        html.P('${0:,.0f}'.format(bitcoincash_market_cap),
                               style = {'textAlign': 'left',
                                        'color': 'black',
                                        'fontSize': 12,
                                        'margin-top': '10px',
                                        }),
                    ),
                ], className = 'hover_only_row'),
            ])
        ], className = 'table_style'),
    ]

@app.callback(Output('bitcoin_chart', 'figure'),
              [Input('update_value', 'n_intervals')])
def update_graph(n_intervals):
    header_list = ['Time', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']
    bitcoin_df = pd.read_csv('bitcoin_data.csv', names = header_list)
    bitcoin_price = bitcoin_df['Price'].tail(30)
    time_interval = bitcoin_df['Time'].tail(30)
    if n_intervals == 0:
        raise PreventUpdate

    return {
        'data': [go.Scatter(
            x = time_interval,
            y = bitcoin_price,
            mode = 'lines',
            line = dict(width = 2, color = '#EC1E3D '),
            # marker = dict(size = 7, symbol = 'circle', color = '#D35400',
            #               line = dict(color = '#D35400', width = 2)
            #               ),

            hoverinfo = 'text',
            hovertext =
            '<b>Time</b>: ' + time_interval.astype(str) + '<br>' +
            '<b>Bitcoin Price</b>: ' + [f'${x:,.2f}' for x in bitcoin_price] + '<br>'

        )],

        'layout': go.Layout(
            # paper_bgcolor = 'rgba(0,0,0,0)',
            # plot_bgcolor = 'rgba(0,0,0,0)',
            plot_bgcolor = 'rgba(255, 255, 255, 0.0)',
            paper_bgcolor = 'rgba(255, 255, 255, 0.0)',
            title = {
                'text': 'Bitcoin Price',

                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': 'black',
                'size': 17},

            hovermode = 'x unified',
            margin = dict(t = 25, r = 10, l = 70),

            xaxis = dict(range = [min(time_interval), max(time_interval)],
                         title = '<b>Time</b>',
                         color = 'black',
                         showspikes=True,
                         showline = True,
                         showgrid = False,
                         linecolor = 'black',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

            yaxis = dict(
                         title = '<b></b>',
                         color = 'black',
                         showspikes=False,
                         showline = True,
                         showgrid = True,
                         linecolor = 'black',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'black')

                         ),

            legend = {
                'orientation': 'h',
                'bgcolor': '#F2F2F2',
                'x': 0.5,
                'y': 1.25,
                'xanchor': 'center',
                'yanchor': 'top'},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'black')

        )

            }

if __name__ == "__main__":
    app.run_server(debug = True)
