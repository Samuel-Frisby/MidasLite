import yfinance as yf

def get_stock_summary(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "price": info.get("regularMarketPrice"),
        "pe_ratio": info.get("trailingPE"),
        "market_cap": info.get("marketCap"),
        "dividend_yield": info.get("dividendYield")
    }