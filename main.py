import numpy as np
from dotenv import load_dotenv
import os
import requests
import pandas as pd

load_dotenv()  # take environment variables from .env.

token = os.getenv('marketdata_token')

# Get stocks

# Get option chain for each stock

# Analyze the stock

# The API endpoint for retrieving stock quotes for SPY
url = 'https://api.marketdata.app/v1/stocks/quotes/SPY/'

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
    print(data)
else:
    print(f'Failed to retrieve data: {response.status_code}')

response = pd.read_json('company_tickers.json')

print(response)