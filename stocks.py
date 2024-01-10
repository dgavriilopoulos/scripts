import yfinance as yf
from datetime import datetime,timedelta

import yfinance as yf
import argparse
from datetime import datetime, timedelta

def get_stock_data(stock_symbols):
    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')

    stock_data = {}

    for symbol in stock_symbols:
        try:
            # Fetch data for each stock
            data = yf.download(symbol, start=current_date, end=current_date)
            stock_data[symbol] = data['Adj Close'].iloc[0]
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")

    return stock_data

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Fetch stock data using yfinance")
    parser.add_argument("symbols", nargs="+", help="List of stock symbols to fetch data for")

    # Parse command-line arguments
    args = parser.parse_args()

    # Get stock data
    stock_data = get_stock_data(args.symbols)

    # Display the fetched data
    print("Stock data for the given symbols:")
    for symbol, close_price in stock_data.items():
        print(f"{symbol}: {close_price}")

