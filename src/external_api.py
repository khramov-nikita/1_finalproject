import json
import os

import requests
from dotenv import load_dotenv

path = os.path.dirname(__file__)
settings_path = os.path.join(path[:-3], "data", "user_settings.json")


def get_currency_rates() -> list:
    """
    Функция отправляет запрос на www.cbr-xml-daily.ru и получает курс валют
    """
    load_dotenv()
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    with open(settings_path, "r") as f:
        settings = json.load(f)
    result = []
    for key in settings["user_currencies"]:
        result.append({"currency": key, "rate": str(round(float(data["Valute"][key]["Value"]), 2))})
    return result


def get_stock_prices() -> list:
    """
    Функция отправляет запрос на www.alphavantage.co и получает акции
    """
    load_dotenv()
    with open(settings_path, "r") as f:
        settings = json.load(f)
    url_list = []
    data = []
    data_raw = []
    result = []

    for key in settings["user_stocks"]:

        url_list.append(
            f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={key}&apikey={os.getenv("API_KEY_STOCK")}'
        )
    for url in url_list:
        data.append(requests.get(url))

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
