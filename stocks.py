import yfinance as yf
import argparse
from datetime import datetime, timedelta

def get_stock_data(stock_symbols):
    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')
    last_week_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')


    stock_data = {}

    for symbol in stock_symbols:
        try:
            # Fetch data for each stock for current date
            data = yf.download(symbol, start=current_date, end=current_date)
            close_price = data['Adj Close'].iloc[0]
            open_price = data['Open'].iloc[0]
            # stock_data[symbol] = {'Open': open_price, 'Close': close_price,'Delta': delta, 'Sign': sign}

            # last_week_data = yf.download(symbol, start=last_week_date)
            # last_week_close_price = data['Close'].iloc[0]
            # last_week_open_price = data['Open'].iloc[0] 
            
            delta = close_price - open_price
            sign = "Positive" if delta >= 0 else "Negative"

            stock_data[symbol] = {
                'Today': {'Open': open_price, 'Close': close_price,'Delta':delta,'Sign':sign},
                # 'LastWeek': {'Open': last_week_open_price,'Delta':delta,'Sign':sign}
            }
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

    #print the current date this is pulled
    print(f"Stock data analysis as of {datetime.now().strftime('%Y-%m-%d')}:")

    # Display the fetched data
    print("Trending Stock data for the given symbols:")
    for symbol, prices in stock_data.items():
        today_open = prices['Today']['Open']
        today_close = prices['Today']['Close']
        today_sign = prices['Today']['Sign']
        # last_week_open = prices['LastWeek']['Open']
        # last_week_close = prices['LastWeek']['Close']
        # last_week_sign = prices['LastWeek']['Sign']


        formatted_delta_today = f"{today_close - today_open:.3f}"
        # formatted_delta_last_week = f"{last_week_close - last_week_open:.3f}"
        
        print(f"{symbol}: Today - Open: {today_open:.3f}, Close: {today_close:.3f}, Delta: {formatted_delta_today} = {today_sign}")