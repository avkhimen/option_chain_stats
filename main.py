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

token = os.getenv('marketdata_token')

for ticker in tickers[:1]:

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
        print(ask)
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
        print(data.keys())
        print(data['expiration'])
        strikes = data['strike']
    else:
        print(f'Failed to retrieve data: {response.status_code}')
        strikes = -1

    print(ask, strikes)
    if ask != -1 and strikes != -1:
        
        index = next((i for i, strike in enumerate(strikes) if float(strike) > ask), -1)
        last_strike = strikes[index]
        expiration = datetime.datetime.fromtimestamp(int(strikes[0])).strftime('%Y-%m-%d %H:%M:%S')

    time.sleep(0.1)