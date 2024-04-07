import yfinance as yf
from datetime import datetime
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()  # take environment variables from .env.

response = pd.read_json('company_tickers.json')

tickers = []

for k, v in response.items():
    tickers.append(v['ticker'])

date_string1 = '2024-04-12'
date_object1 = datetime.strptime(date_string1, '%Y-%m-%d')

date_string2 = '2024-04-14'
date_object2 = datetime.strptime(date_string2, '%Y-%m-%d')

print((date_object2 - date_object1).days)

aapl = yf.Ticker("SPY")

print(aapl.info['fiftyTwoWeekHigh'])
print(aapl.options)
print(aapl.info.keys())

try:
    ticker_obj = yf.Ticker("FDFHFDGHFGH")
    ticker_exists = True
except Exception as e:
    ticker_exists = False

# Things to consider
# difference between options
# Last price
# percentage of low price against high
# ticker
# difference between option legs
# frequency of options
# 1st call strike
# 2nd call strike
# 1 put strike
# 2nd put strike
# 1st call price
# 2nd call price
# 1 put price
# 2 put price
# expiration
# delta
# implied volatility
# average high-low
# average open - low
# average high - open
# average high - low
# percent over 1st call
# percent over 2nd call
# percent under 1st put
# percent under 2nd put
# average potential revenue per month 1st call
# average potential revenue per month 2nd call
# average potential revenue per month 1st put
# average potential revenue per month 2nd put