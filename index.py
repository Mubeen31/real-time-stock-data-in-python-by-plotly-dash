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
        dcc.Interval(id = 'update_value',
                     interval = 3000,
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

], id= "mainContainer",
   style={"display": "flex", "flex-direction": "column"})

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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
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
                    html.P('Market Cap:' + '${0:,.0f}'.format(market_cap),
                           style = {'textAlign': 'left',
                                    'color': '#808080',
                                    'fontSize': 12,
                                    'margin-top': '-8px',
                                    }, className = 'margin_left_value_row2'
                           ),
                ], className = 'adjust_price_row2')

            ]


if __name__ == "__main__":
    app.run_server(debug = True)
