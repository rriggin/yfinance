import yfinance as yf

def get_options_chain(ticker_symbol):
    # Create a Ticker object for the given symbol
    ticker = yf.Ticker(ticker_symbol)
    
    # Retrieve the current stock price
    stock_price = ticker.history(period="1d")['Close'].iloc[-1]
    print(f"Current stock price for {ticker_symbol}: ${stock_price:.2f}\n")
    
    # Retrieve available expiration dates for the options
    expiration_dates = ticker.options
    
    # Check if there are any expiration dates available
    if expiration_dates:
        # Fetch the options chain for the first expiration date
        options_chain = ticker.option_chain(expiration_dates[0])
        
        # Print the calls and puts data
        print("Calls:\n", options_chain.calls)
        print("\nPuts:\n", options_chain.puts)
    else:
        # Inform the user if no options data is available
        print(f"No options data available for {ticker_symbol}")

if __name__ == "__main__":
    # Call the function with a sample ticker symbol
    get_options_chain('DKNG')