import os

import requests
from dotenv import load_dotenv


def get_currency_rates() -> list:
    load_dotenv()
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    result = [
        {"currency": "USD", "rate": str(round(float(data["Valute"]["USD"]["Value"]), 2))},
        {"currency": "EUR", "rate": str(round(float(data["Valute"]["EUR"]["Value"]), 2))},
    ]
    return result


def get_stock_prices() -> list:
    load_dotenv()
    url_aapl = (
        f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey={os.getenv("API_KEY_STOCK")}'
    )
    url_amzn = (
        f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AMZN&apikey={os.getenv("API_KEY_STOCK")}'
    )
    url_googl = (
        f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=GOOGL&apikey={os.getenv("API_KEY_STOCK")}'
    )
    url_msft = (
        f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MSFT&apikey={os.getenv("API_KEY_STOCK")}'
    )
    url_tsla = (
        f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=TSLA&apikey={os.getenv("API_KEY_STOCK")}'
    )

    aapl = requests.get(url_aapl)
    amzn = requests.get(url_amzn)
    googl = requests.get(url_googl)
    msft = requests.get(url_msft)
    tsla = requests.get(url_tsla)

    data = [aapl, amzn, googl, msft, tsla]
    data_raw = []
    result = []

    for url in data:
        data_raw.append(url.json())

    for item in data_raw:
        result.append(
            {
                "stock": item["Global Quote"]["01. symbol"],
                "price": str(round(float(item["Global Quote"]["05. price"]), 2)),
            }
        )
    return result
