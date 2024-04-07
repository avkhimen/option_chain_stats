import yfinance as yf
from datetime import datetime

date_string1 = '2024-04-12'
date_object1 = datetime.strptime(date_string1, '%Y-%m-%d')

date_string2 = '2024-04-14'
date_object2 = datetime.strptime(date_string2, '%Y-%m-%d')

print((date_object2 - date_object1).days)

aapl = yf.Ticker("AAPL")

print(aapl.info['fiftyTwoWeekHigh'])

# Things to consider
# difference between options
# Last price
# percentage of low price against high
# ticker
# difference between option legs
# 1st call strike
# 2nd call strike
# 1 put strike
# 2nd put strike
# 1st call price
# 2nd call price
# 1 put price
# 2 put price
