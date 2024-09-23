import yfinance as yf
import pandas as pd

# Assuming 'EQUITY_L.csv' is in the same directory as this script
all_stocks = pd.read_csv('EQUITY_L.csv')

def correct_format(s: str) -> str:
    """
    Capitalize the first letter of each word in the string,
    leaving the rest of the letters unchanged.
    """
    return ' '.join(word[0].upper() + word[1:] for word in s.split()) + ' Limited'

def fetch_tickers(stock_name: str):
    stock_name = correct_format(stock_name)
    filter = all_stocks['NAME OF COMPANY'] == stock_name
    ticker = all_stocks[filter]['SYMBOL'].values
    return ticker[0] if len(ticker) > 0 else None

def fetch_price(symbol: str):
    ticker_symbol = fetch_tickers(symbol)
    if ticker_symbol is None:
        return "Stock not found"
    ticker = yf.Ticker(f"{ticker_symbol}.NS")
    data = ticker.history(period="1d", interval='1m')
    if data.empty:
        return "No data available"
    current_price = data['Close'].iloc[-1]
    return f'{current_price:.2f}'

if __name__=='__main__':
    fetch_price()