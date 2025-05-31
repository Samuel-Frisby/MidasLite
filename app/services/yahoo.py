import yfinance as yf

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