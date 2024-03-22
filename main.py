import numpy as np
from dotenv import load_dotenv
import os
import requests
import pandas as pd
import time

load_dotenv()  # take environment variables from .env.

response = pd.read_json('company_tickers.json')

tickers = []

for k, v in response.items():
    tickers.append(v['ticker'])

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
        ask = data['ask'][0]
    else:
        print(f'Failed to retrieve data: {response.status_code}')

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
        strikes = data['strike']
        i = 0
        for strike in strikes:
            while strike <= ask:
                i += 1
        last_strike = strikes[i]
        print(last_strike)
    else:
        print(f'Failed to retrieve data: {response.status_code}')

    time.sleep(0.1)