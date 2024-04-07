import yfinance as yf
from datetime import datetime

date_string1 = '2024-04-12'
date_object1 = datetime.strptime(date_string1, '%Y-%m-%d')

date_string2 = '2024-04-14'
date_object2 = datetime.strptime(date_string2, '%Y-%m-%d')

print((date_object2 - date_object1).days)

aapl = yf.Ticker("AAPL")

print(aapl.options)