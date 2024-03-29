import numpy as np
from dotenv import load_dotenv
import os
import requests
import pandas as pd
import time
import datetime

load_dotenv()  # take environment variables from .env.

response = pd.read_json('company_tickers.json')

tickers = []

for k, v in response.items():
    tickers.append(v['ticker'])

#tickers = ['RIOT', 'AAPL', 'PLTR']

token = os.getenv('marketdata_token')

for ticker in tickers:

    # The API endpoint for retrieving stock quotes for SPY
    url = 'https://api.marketdata.app/v1/stocks/quotes/' + ticker + '/'

    # Setting up the headers for authentication
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Making the GET request to the API
    response = requests.get(url, headers=headers)

    # Checking if the request was successful
    if response. status_code in (200, 203):
        # Parsing the JSON response
        data = response.json()
        ask = float(data['ask'][0])
        #print(ask)
    else:
        print(f'Failed to retrieve data: {response.status_code}')
        ask = -1

    url = 'https://api.marketdata.app/v1/options/chain/' + ticker + '/'

        # Setting up the headers for authentication
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Making the GET request to the API
    response = requests.get(url, headers=headers)

        # Checking if the request was successful
    if response. status_code in (200, 203):
        # Parsing the JSON response
        data = response.json()
        #print(data.keys())
        #print(data)
        #print(data['expiration'])
        strikes = data['strike']
    else:
        print(f'Failed to retrieve data: {response.status_code}')
        strikes = -1

    #print(ask, strikes)
    if ask != -1 and strikes != -1:
        
        index = next((i for i, strike in enumerate(strikes) if float(strike) > ask), -1)
        last_strike = str(float(strikes[index]))
        expiration = str(datetime.datetime.fromtimestamp(int(data['expiration'][index])).strftime('%Y-%m-%d %H:%M:%S'))
        call_bid = str(float(data['bid'][index]))
        call_ask = str(float(data['ask'][index]))
        iv = str(float(data['iv'][index]))

        # print(index)
        # print(last_strike)
        # print(expiration)
        # print(call_ask)
        # print(call_bid)
        # print(data['strike'][index])
        # print(iv)
        print(ticker, '|', ask, '|', last_strike, '|', expiration, '|', call_ask, '|', call_bid, '|', iv)
        s = ticker + '|' + ask + '|' + last_strike + '|' + expiration + '|' + call_ask + '|' + call_bid + '|' + iv
        with open('data.txt', 'wb') as f:
            f.write(s)

    time.sleep(1)