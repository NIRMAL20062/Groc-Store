import requests
from bs4 import BeautifulSoup
import time

# Headers to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def scrape_amazon(product):
    url = f"https://www.amazon.com/s?k={product.replace(' ', '+')}"
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        price = soup.select_one(".a-price-whole")
        return float(price.text.replace(",", "")) if price else None
    except Exception as e:
        print(f"Amazon scrape error: {e}")
        return None

def scrape_ebay(product):
    url = f"https://www.ebay.com/sch/i.html?_nkw={product.replace(' ', '+')}"
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")
        price = soup.select_one(".s-item__price")
        return float(price.text.replace("$", "").replace(",", "")) if price else None
    except Exception as e:
        print(f"eBay scrape error: {e}")
        return None

def get_prices(product):
    prices = {
        "amazon": scrape_amazon(product) or 0.0,
        "ebay": scrape_ebay(product) or 0.0
    }
    return prices

# Simulate price history (in a real app, store this in a database)
def get_price_history(product):
    import pandas as pd
    # Dummy data for now
    dates = pd.date_range(end="2025-03-03", periods=5).strftime("%Y-%m-%d").tolist()
    prices = {
        "amazon": [100, 102, 99, 101, 100],
        "ebay": [98, 97, 96, 95, 94]
    }
    return {"dates": dates, "prices": prices}

if __name__ == "__main__":
    product = "laptop"
    prices = get_prices(product)
    history = get_price_history(product)
    print(f"Prices: {prices}")
    print(f"History: {history}")