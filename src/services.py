import logging
import os

from src.processing import count_categories
from src.utils import return_dict_to_json

path = os.path.dirname(__file__)
log_path = os.path.join(path[:-3], "logs", "services.log")
json_path = os.path.join(path[:-3], "data", "cashback.json")
operations_path = os.path.join(path[:-3], "data", "operations.xlsx")


app_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(filename=log_path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
app_logger.addHandler(file_handler)
app_logger.setLevel(logging.DEBUG)


def cashback_categories(data: list, year: str, month: str) -> None:
    """
    Функция подсчитывает бонус по каждой категории в указанном диапазоне времени
    """
    try:
        app_logger.info("Начало работы функции подсчёта кешбека")
        categories_dict = count_categories(data, year, month)
        return_dict_to_json(categories_dict, json_path)
    except Exception as e:
        app_logger.error(f"Неудачная попытка подсчёта кешбека: {e}")
        raise e
    else:
        return
