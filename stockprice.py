import yfinance as yf
import pandas as pd
from colorama import Fore
from mcp.server.fastmcp import FastMCP

mcp = FastMCP('yfinanceserver')
@mcp.tool()
def stock_price(stock_ticker: str) -> pd.DataFrame:
    """
    Fetches the stock price data for the given stock ticker.
    
    Args:
        stock_ticker (str): The stock ticker symbol.
        
    Returns:
        pd.DataFrame: A DataFrame containing the stock price data.
    """
    data = yf.Ticker(stock_ticker)
    prices = data.history(period="1mo")
    return prices
stock_ticker = "IBM" 

data = yf.Ticker(stock_ticker)
prices=data.history(period="1mo")
print(Fore.GREEN + "Stock Price Data for the last month:"+str(prices) + Fore.RESET)

if __name__ == "__main__":
    mcp.run(transport='stdio')
