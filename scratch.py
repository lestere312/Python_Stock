# Import yfinance
import yfinance as yf
import pandas as pd

data = yf.download("ABEV3.SA", start="2020-08-01", end="2020-08-30")

print(type(data))
print(data)

print(data['High'])
print(data[['Low']])
print(data.iloc[1])
print(data.iloc[1][0])

tickers = {"F", "WFC", "GM"}

for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_quote = (data.tail(1)['Close'].iloc[0])
    print(ticker,last_quote)
