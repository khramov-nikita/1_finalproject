import datetime
import logging
import os

from src.external_api import get_currency_rates, get_stock_prices
from src.processing import get_cards, get_greeting, get_top_transactions, set_date
from src.utils import read_xlsx, return_dict_to_json

path = os.path.abspath(__file__)
log_path = os.path.join(path[:-13], "logs", "views.log")
json_path = os.path.join(path[:-13], "data", "main_page.json")
operations_path = os.path.join(path[:-13], "data", "operations.xlsx")

app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(filename=log_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


def get_main_page() -> None:
    """
    Функция выгружает json ответ для главной станицы
    """
    date_time = datetime.datetime.now()
    hour = int(date_time.hour)
    data = set_date(
        read_xlsx(operations_path), input("Введите дату, по которую будут показаны операции (enter - текущая дата): ")
    )
    result = {
        "greeting": get_greeting(hour),
        "cards": get_cards(data),
        "top_transactions": get_top_transactions(data),
        "currency_rates": get_currency_rates(),
        "stock_prices": get_stock_prices(),
    }
    return_dict_to_json(result, json_path)


if __name__ == "__main__":
    get_main_page()
