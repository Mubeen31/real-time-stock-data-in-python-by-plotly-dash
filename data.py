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
    # print(df)
    # print(df[0])
    # print(df[0].columns)

    # Remove column
    df[0].drop(df[0].columns[[4, 5, 7]], axis = 1, inplace = True)
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
    df[0] = df[0][['Rank', 'CryptoCurrency', 'Price', 'Change (24h) %', 'Market Cap.']]
    # print(df[0])

    time.sleep(5)
    # print(df[0].dtypes)

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    bitcoin_row = df[0]
    # print(bitcoin_row)
    bitcoin_rank = bitcoin_row[bitcoin_row['CryptoCurrency'] == 'Bitcoin']['Rank'].iloc[0]
    bitcoin_currency = bitcoin_row[bitcoin_row['CryptoCurrency'] == 'Bitcoin']['CryptoCurrency'].iloc[0]
    bitcoin_price = bitcoin_row[bitcoin_row['CryptoCurrency'] == 'Bitcoin']['Price'].iloc[0]
    bitcoin_change = bitcoin_row[bitcoin_row['CryptoCurrency'] == 'Bitcoin']['Change (24h) %'].iloc[0]
    bitcoin_market_cap = bitcoin_row[bitcoin_row['CryptoCurrency'] == 'Bitcoin']['Market Cap.'].iloc[0]

    ethereum_row = df[0]
    ethereum_rank = ethereum_row[ethereum_row['CryptoCurrency'] == 'Ethereum']['Rank'].iloc[0]
    ethereum_currency = ethereum_row[ethereum_row['CryptoCurrency'] == 'Ethereum']['CryptoCurrency'].iloc[0]
    ethereum_price = ethereum_row[ethereum_row['CryptoCurrency'] == 'Ethereum']['Price'].iloc[0]
    ethereum_change = ethereum_row[ethereum_row['CryptoCurrency'] == 'Ethereum']['Change (24h) %'].iloc[0]
    ethereum_market_cap = ethereum_row[ethereum_row['CryptoCurrency'] == 'Ethereum']['Market Cap.'].iloc[0]

    binance_row = df[0]
    binance_rank = binance_row[binance_row['CryptoCurrency'] == 'BNB']['Rank'].iloc[0]
    binance_currency = binance_row[binance_row['CryptoCurrency'] == 'BNB']['CryptoCurrency'].iloc[0]
    binance_price = binance_row[binance_row['CryptoCurrency'] == 'BNB']['Price'].iloc[0]
    binance_change = binance_row[binance_row['CryptoCurrency'] == 'BNB']['Change (24h) %'].iloc[0]
    binance_market_cap = binance_row[binance_row['CryptoCurrency'] == 'BNB']['Market Cap.'].iloc[0]
    # print(df[0].head(30))

    bitCoinCash_row = df[0]
    bitCoinCash_rank = bitCoinCash_row[bitCoinCash_row['CryptoCurrency'] == 'Bitcoin Cash']['Rank'].iloc[0]
    bitCoinCash_currency = bitCoinCash_row[bitCoinCash_row['CryptoCurrency'] == 'Bitcoin Cash']['CryptoCurrency'].iloc[0]
    bitCoinCash_price = bitCoinCash_row[bitCoinCash_row['CryptoCurrency'] == 'Bitcoin Cash']['Price'].iloc[0]
    bitCoinCash_change = bitCoinCash_row[bitCoinCash_row['CryptoCurrency'] == 'Bitcoin Cash']['Change (24h) %'].iloc[0]
    bitCoinCash_market_cap = bitCoinCash_row[bitCoinCash_row['CryptoCurrency'] == 'Bitcoin Cash']['Market Cap.'].iloc[0]
    # print(df[0].head(30))

    chainLink_row = df[0]
    chainLink_rank = chainLink_row[chainLink_row['CryptoCurrency'] == 'Chainlink']['Rank'].iloc[0]
    chainLink_currency = chainLink_row[chainLink_row['CryptoCurrency'] == 'Chainlink']['CryptoCurrency'].iloc[0]
    chainLink_price = chainLink_row[chainLink_row['CryptoCurrency'] == 'Chainlink']['Price'].iloc[0]
    chainLink_change = chainLink_row[chainLink_row['CryptoCurrency'] == 'Chainlink']['Change (24h) %'].iloc[0]
    chainLink_market_cap = chainLink_row[chainLink_row['CryptoCurrency'] == 'Chainlink']['Market Cap.'].iloc[0]

    with open("bitcoin_data.csv", "a") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, bitcoin_rank, bitcoin_currency, bitcoin_price, bitcoin_change, bitcoin_market_cap])
        # print(dt_string, bitcoin_rank, bitcoin_currency, bitcoin_price, bitcoin_change, bitcoin_market_cap)
    with open("ethereum_data.csv", "a") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, ethereum_rank, ethereum_currency, ethereum_price, ethereum_change, ethereum_market_cap])
        # print(dt_string, ethereum_rank, ethereum_currency, ethereum_price, ethereum_change, ethereum_market_cap)
    with open("binance_data.csv", "a") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, binance_rank, binance_currency, binance_price, binance_change, binance_market_cap])
        # print(dt_string, binance_rank, binance_currency, binance_price, binance_change, binance_market_cap)
    with open("bitcoincash_data.csv", "a") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, bitCoinCash_rank, bitCoinCash_currency, bitCoinCash_price, bitCoinCash_change, bitCoinCash_market_cap])
        print(dt_string, bitCoinCash_rank, bitCoinCash_currency, bitCoinCash_price, bitCoinCash_change, bitCoinCash_market_cap)
    with open("chainlink_data.csv", "a") as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([dt_string, chainLink_rank, chainLink_currency, chainLink_price, chainLink_change, chainLink_market_cap])
        # print(dt_string, chainLink_rank, chainLink_currency, chainLink_price, chainLink_change, chainLink_market_cap)

