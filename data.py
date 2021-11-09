import pandas as pd
from urllib.request import Request, urlopen
import time
import csv
from datetime import datetime
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


i = 1
while i == 1:
    url = 'https://goldprice.org/cryptocurrency-price'
    import_request = Request(url, headers = {'User-Agent': 'Chrome/91.0.4472.77'})
    web_page_data = urlopen(import_request).read()
    df = pd.read_html(web_page_data)
    # print(df[0])
    # print(df[0].columns)

    # Remove column
    df[0].drop(df[0].columns[[0, 4, 5, 7]], axis = 1, inplace = True)
    # print(df[0].columns)

    # Rename column
    df[0].rename(columns = {'Change (24h)': 'Change (24h) %'}, inplace = True)

    # Remove % and $ symbols from columns
    df[0]['Price'] = list(map(lambda x: x[1:], df[0]['Price'].values))
    df[0]['Change (24h) %'] = list(map(lambda x: x[:-1], df[0]['Change (24h) %'].values))
    df[0]['Market Cap.'] = list(map(lambda x: x[1:], df[0]['Market Cap.'].values))

    # Remove commas from columns
    df[0]['Price'] = df[0]['Price'].str.replace(',', '')
    df[0]['Market Cap.'] = df[0]['Market Cap.'].str.replace(',', '')

    # Change data type of column
    df[0]['Price'] = df[0]['Price'].astype(float).round(2)
    df[0]['Change (24h) %'] = df[0]['Change (24h) %'].astype(float)
    df[0]['Market Cap.'] = df[0]['Market Cap.'].astype('int64')

    # Change position of columns
    df[0] = df[0][['CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']]

    time.sleep(5)
    # print(df[0].dtypes)

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    bitcoin_row = df[0].loc[[0]]
    bitcoin_currency = bitcoin_row['CryptoCurrency'][0]
    bitcoin_price = bitcoin_row['Price'][0]
    bitcoin_change = bitcoin_row['Change (24h) %'][0]
    bitcoin_market_cap = bitcoin_row['Market Cap.'][0]

    ethereum_row = df[0].loc[[1]]
    ethereum_currency = ethereum_row['CryptoCurrency'][1]
    ethereum_price = ethereum_row['Price'][1]
    ethereum_change = ethereum_row['Change (24h) %'][1]
    ethereum_market_cap = ethereum_row['Market Cap.'][1]

    binance_row = df[0].loc[[2]]
    binance_currency = binance_row['CryptoCurrency'][2]
    binance_price = binance_row['Price'][2]
    binance_change = binance_row['Change (24h) %'][2]
    binance_market_cap = binance_row['Market Cap.'][2]
    # print(df[0].head(30))

    bitcoincash_row = df[0].loc[[18]]
    bitcoincash_currency = bitcoincash_row['CryptoCurrency'][18]
    bitcoincash_price = bitcoincash_row['Price'][18]
    bitcoincash_change = bitcoincash_row['Change (24h) %'][18]
    bitcoincash_market_cap = bitcoincash_row['Market Cap.'][18]
    # print(df[0].head(30))

    chainlink_row = df[0].loc[[12]]
    chainlink_currency = chainlink_row['CryptoCurrency'][12]
    chainlink_price = chainlink_row['Price'][12]
    chainlink_change = chainlink_row['Change (24h) %'][12]
    chainlink_market_cap = chainlink_row['Market Cap.'][12]

    with open("bitcoin_data.csv", "a") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, bitcoin_currency, bitcoin_price, bitcoin_change, bitcoin_market_cap])
        print(dt_string, bitcoin_currency, bitcoin_price, bitcoin_change, bitcoin_market_cap)
    with open("ethereum_data.csv", "a") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, ethereum_currency, ethereum_price, ethereum_change, ethereum_market_cap])
    #     # print(dt_string, ethereum_currency, ethereum_price, ethereum_change, ethereum_market_cap)
    with open("binance_data.csv", "a") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, binance_currency, binance_price, binance_change, binance_market_cap])
    #     # print(dt_string, binance_currency, binance_price, binance_change, binance_market_cap)
    with open("bitcoincash_data.csv", "a") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, bitcoincash_currency, bitcoincash_price, bitcoincash_change, bitcoincash_market_cap])
        # print(dt_string, bitcoincash_currency, bitcoincash_price, bitcoincash_change, bitcoincash_market_cap)
    with open("chainlink_data.csv", "a") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, chainlink_currency, chainlink_price, chainlink_change, chainlink_market_cap])
    #     # print(dt_string, chainlink_currency, chainlink_price, chainlink_change, chainlink_market_cap)
