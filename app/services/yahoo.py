import yfinance as yf
from datetime import datetime, timedelta

def get_stock_summary(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "price": info.get("regularMarketPrice", "N/A"),
            "pe_ratio": info.get("trailingPE", "N/A"),
            "market_cap": info.get("marketCap", "N/A"),
            "dividend_yield": info.get("dividendYield", "N/A")
        }
    except Exception as e:
        print(f"❌ Error fetching data for '{ticker}': {e}")
        return {
            "price": "N/A",
            "pe_ratio": "N/A",
            "market_cap": "N/A",
            "dividend_yield": "N/A"
        }
    

def get_stock_history(ticker: str, period="1mo", interval="1d"):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)
        hist.reset_index(inplace=True)
        hist = hist[["Date", "Close"]]
        hist["Date"] = hist["Date"].astype(str)
        return hist.to_dict(orient="records")
    except Exception as e:
        print(f"❌ Error fetching history for '{ticker}': {e}")
        return []